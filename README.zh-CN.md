# 🛡️ Hermes 铠甲

**给 Hermes Agent 装上安全底座 — 从哲学出发，用代码落地。**

<img src="assets/logo.jpeg" alt="Hermes 铠甲" width="100%">

一个完整的安全增强套件，让 Hermes Agent：
- **看得懂** — 操作前用大白话解释它在做什么
- **控得住** — Tirith 引擎硬控危险命令
- **藏得深** — 网络请求分级，保护本地 IP
- **稳得住** — 出错时拦截而非放行，不确定时暂停而非猜测

---

## 📦 包含什么

```
hermes-armor/
├── SKILL.md                 # 🧠 核心 — 行为宪法 + 执行规则
├── install.sh               # 🚀 一键安装
├── gatekeeper.py            # 🚪 门神脚本（网络出口 + 文件保护）
├── assets/
│   └── logo.jpeg            # 项目图标
├── config/
│   └── policy.yaml          # ⚙️ Tirith 策略
├── scripts/
│   └── post-update-check.sh # 🔍 更新后检查
└── docs/
    └── 架构说明.md           # 📖 架构文档
```

## 🚀 快速安装

```bash
curl -fsSL https://raw.githubusercontent.com/ArtiNexus/hermes-armor/main/install.sh | bash
```

## 📜 行为宪法（四条）

1. **绝对安全原则** — 不可逾越的底线
2. **损失最小化原则** — 宁可停不可错
3. **利益最大化原则** — 本地优先、成本最优
4. **操作可见性原则** — 你看得懂才是真的懂

## 🔧 要求

- Hermes Agent（任何版本）
- macOS / Linux
- Tirith 0.2.10+（安装脚本会自动安装）

## 🔄 Hermes 更新后

```bash
bash ~/.hermes/skills/dogfood/hermes-armor/scripts/post-update-check.sh
```

## 📄 许可证

MIT
