#!/usr/bin/env python3
"""
Hermes 铠甲 — 门神脚本 v3

职责分层:
  Tirith: 命令安全扫描（同形攻击、管道注入、数据外泄等）
  gatekeeper: 网络出口分级 + 文件操作保护 + 禁止命令过滤

顶层宪法:
  第一条 绝对安全 — 不可逾越的底线
  第二条 损失最小 — 宁可停不可错
  第三条 利益最大 — 资源最优、本地优先
"""

import sys
import re
import json

# ================================================================
# 🟢 白名单 — 本地网络直连（宪法第三条：利益最大）
# 只有确认可信的源才走本地网络
# ================================================================
WHITELIST_DOMAINS = [
    # 包管理/代码源
    "pypi.org", "files.pythonhosted.org",
    "github.com", "raw.githubusercontent.com",
    "npmjs.org", "registry.npmjs.org",
    "brew.sh", "docker.com", "docker.io",
    # 日常访问（你说的）
    "csdn.net", "juejin.cn", "zhihu.com",
    "xiaohongshu.com", "youtube.com",
    # 学习
    "docs.python.org", "docs.dify.ai",
]

# ================================================================
# 🔴 黑名单 — 直接拦截（宪法第一条：绝对安全）
# ================================================================
BLACKLIST_DOMAINS = [
    "*.xyz", "*.top", "*.gq", "*.ml", "*.cf", "*.tk", "*.icu",
    "*.doubleclick.net", "*.googleadservices.com",
]

# ================================================================
# 🟠 敏感场景 — 触发时强制走远程浏览器（宪法第二条：损失最小）
# 不直接拦截，但升级网络出口
# ================================================================
SENSITIVE_SCENARIOS = {
    # 场景: 访问暗网/匿名网络相关
    "darkweb": {
        "keywords": ["暗网", "dark.?web", "darknet", "tor", "onion"],
        "action": "upgrade",
        "reason": "涉及暗网/匿名网络，强制远程浏览器"
    },
    # 场景: 涉及破解/盗版
    "crack": {
        "keywords": ["破解", "crack", "盗版", "warez"],
        "action": "upgrade",
        "reason": "涉及破解/盗版内容，强制远程浏览器"
    },
}

# ================================================================
# 🚫 禁止命令（宪法第一条：绝对安全）
# 不是针对命令本身，而是针对危险的使用方式
# ================================================================
FORBIDDEN_PATTERNS = [
    # 毁灭性操作
    (r'\brm\s+-rf\s+/\b', "禁止删除根目录"),
    (r'\brm\s+-rf\s+~(?:\s|$)', "禁止删除用户目录"),
    # 向未知目标发送本地文件
    (r'curl\s+.*\s+-[Td]\s+', "禁止通过 curl 上传本地文件到未知目标"),
    (r'wget\s+.*\s+--post-file\s*=', "禁止通过 wget 上传本地文件"),
    # 修改 hermes 自身配置
    (r'[~\/]\.hermes\/config\.yaml', "禁止修改 Hermes 配置文件"),
]

# ================================================================
# 🛡️ 受保护路径（宪法第一条：绝对安全）
# ================================================================
PROTECTED_PATHS = [
    "/etc/", "/System/", "/Library/",
    "/.hermes/", "~/.hermes/",
]


def domain_from_url(url: str) -> str | None:
    m = re.search(r'https?://([^/]+)', url)
    return m.group(1) if m else None


def match_domain(domain: str, pattern: str) -> bool:
    if pattern.startswith("*."):
        return domain.endswith(pattern[1:]) or domain == pattern[2:]
    return domain == pattern


def check_whitelist(url: str) -> bool:
    domain = domain_from_url(url)
    if not domain:
        return False
    return any(match_domain(domain, wl) for wl in WHITELIST_DOMAINS)


def check_blacklist(url: str) -> bool:
    domain = domain_from_url(url)
    if not domain:
        return False
    return any(match_domain(domain, bl) for bl in BLACKLIST_DOMAINS)


def check_sensitive(text: str):
    """检查是否命中敏感场景"""
    for scenario_name, scenario in SENSITIVE_SCENARIOS.items():
        for kw in scenario["keywords"]:
            if re.search(kw, text.lower()):
                return scenario["action"], scenario["reason"]
    return None, None


def check_forbidden(text: str):
    for pattern, reason in FORBIDDEN_PATTERNS:
        if re.search(pattern, text.lower()):
            return True, reason
    return False, None


def check_protected_path(path: str):
    for pp in PROTECTED_PATHS:
        if pp in path:
            return True, pp
    return False, None


def check_action(action: str, target: str, context: str = "") -> dict:
    """
    门神主逻辑
    返回: {"decision": "pass"|"block"|"upgrade"|"ask", "reason": str}
    """
    full_text = target + " " + (context or "")

    # === 宪法第一条：绝对安全 ===

    # F1: 禁止命令模式
    found, reason = check_forbidden(target)
    if found:
        return {"decision": "block", "reason": reason}

    # F2: 受保护路径
    if action == "write":
        found, path = check_protected_path(target)
        if found:
            return {"decision": "block", "reason": f"禁止写入受保护路径: {path}"}

    # === 网络出口检查 ===
    if action in ("network", "search", "execute"):
        url_match = re.search(r'https?://[^\s"\'<>]+', target)
        url = url_match.group(0) if url_match else target

        # 黑名单 → 拦截（第一条）
        if check_blacklist(url):
            return {"decision": "block", "reason": f"目标在黑名单中: {url}"}

        # 敏感场景 → 升级远程浏览器（第二条）
        action_r, reason = check_sensitive(full_text)
        if action_r:
            return {"decision": action_r, "reason": reason}

        # 白名单 → 放行本地直连（第三条）
        if check_whitelist(url):
            return {"decision": "pass", "reason": "白名单域名，本地直连"}

        # 默认 → 远程浏览器（第三条：保护本地 IP）
        return {"decision": "upgrade", "reason": "默认使用远程浏览器保护本地 IP"}

    # === 默认放行 ===
    return {"decision": "pass", "reason": ""}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"decision": "block", "reason": "参数不足"}))
        sys.exit(1)

    result = check_action(sys.argv[1], sys.argv[2],
                          sys.argv[3] if len(sys.argv) > 3 else "")
    print(json.dumps(result, ensure_ascii=False))
