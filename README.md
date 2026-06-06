# 🛡️ Hermes Armor

**A security enhancement suite for Hermes Agent — built on philosophy, enforced by code.**

<img src="assets/logo.png" alt="Hermes Armor" width="100%">

A complete safety layer that makes Hermes Agent:
- **Understandable** — explains what it's doing in plain language before acting
- **Controllable** — hard-blocked dangerous commands via Tirith engine
- **Private** — network requests routed to protect your local IP
- **Resilient** — fails closed, never guesses when uncertain

---

## 📦 What's Inside

```
hermes-armor/
├── SKILL.md                 # 🧠 Core — Constitutional Charter + enforcement rules
├── install.sh               # 🚀 One-click installer
├── gatekeeper.py            # 🚪 Gatekeeper script (network egress + file protection)
├── assets/
│   └── logo.png             # Project logo
├── config/
│   └── policy.yaml          # ⚙️ Tirith policy (allowlist/blocklist/severity overrides)
├── scripts/
│   └── post-update-check.sh # 🔍 Post-update config verification
└── docs/
    └── architecture.md       # 📖 Architecture overview
```

## 🚀 Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/ArtiNexus/hermes-armor/main/install.sh | bash
```

## 📜 Constitutional Charter (4 Articles)

1. **Absolute Safety** — inviolable boundaries. Never bypass Tirith blocks.
2. **Loss Minimization** — better to pause than to break. Enter safe mode on uncertainty.
3. **Utility Maximization** — local-first, cost-optimal. Don't reach for the network unless necessary.
4. **Operational Transparency** — if you can't understand it, it shouldn't run silently. Explain before you act.

## 🔧 Requirements

- Hermes Agent (any version)
- macOS / Linux
- Tirith 0.2.10+ (auto-installed by the script)

## 🔄 After Hermes Update

Run the post-update check to verify your config wasn't overwritten:

```bash
bash ~/.hermes/skills/dogfood/hermes-armor/scripts/post-update-check.sh
```

## 📄 License

MIT
