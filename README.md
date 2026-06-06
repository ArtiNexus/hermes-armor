# 🛡️ Hermes 铠甲

**给 Hermes Agent 装上安全底座。**

一个完整的安全增强套件，包含：
- **行为宪法** — 四条顶层哲学原则，指导 Agent 在不确定场景下如何决策
- **Tirith 策略** — 80+ 内置检测规则配合自定义策略，硬控危险命令
- **门神脚本** — 网络出口分级、文件保护、禁止命令过滤

---

## 📦 包含什么

```
hermes-armor/
├── SKILL.md                 # 🧠 铠甲核心 — 行为宪法 + 执行规则
├── install.sh               # 🚀 一键安装脚本
├── config/
│   └── policy.yaml          # ⚙️ Tirith 策略文件（白名单/黑名单/严重级别覆盖）
├── gatekeeper.py            # 🚪 门神脚本（网络出口分级 + 文件保护）
├── scripts/
│   └── post-update-check.sh # 🔍 Hermes 更新后的配置检查脚本
└── docs/
    └── README.md             # 📖 架构说明
```

## 🚀 快速安装

```bash
# 一键部署
curl -fsSL https://raw.githubusercontent.com/ArtiNexus/hermes-armor/main/install.sh | bash
```

## 📜 行为宪法（四条）

1. **绝对安全原则** — 不可逾越的底线。Tirith 拦截的命令绝不绕过。
2. **损失最小化原则** — 宁可停不可错。连续失败或不确定时进入暂停状态。
3. **利益最大化原则** — 本地优先、成本最优。能本地处理的不联网。
4. **操作可见性原则** — 你看得懂才是真的懂。操作前先说大白话。

## 🔧 要求

- Hermes Agent（任何版本）
- macOS / Linux
- Tirith 0.2.10+（安装脚本会自动安装）

## 🔄 Hermes 更新后

跑一下检查脚本，确认配置没被覆盖：

```bash
bash ~/.hermes/skills/dogfood/hermes-armor/scripts/post-update-check.sh
```

## 📄 许可证

MIT
