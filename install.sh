#!/bin/bash
# 🛡️ Hermes 铠甲 — 一键安装脚本
# 用法: curl -fsSL https://raw.githubusercontent.com/ArtiNexus/hermes-armor/main/install.sh | bash

set -e

echo "🛡️ Hermes 铠甲 — 安装开始"
echo "=========================="

# 1. 备份当前配置
if [ -f ~/.hermes/config.yaml ]; then
  cp ~/.hermes/config.yaml ~/.hermes/config.yaml.bak.hermes-armor
  echo "✅ 已备份 config.yaml"
fi

# 2. 创建 Tirith 策略目录
mkdir -p ~/.config/tirith/
echo "✅ 已创建 Tirith 策略目录"

# 3. 复制策略文件
cp config/policy.yaml ~/.config/tirith/policy.yaml 2>/dev/null || curl -fsSL https://raw.githubusercontent.com/ArtiNexus/hermes-armor/main/config/policy.yaml -o ~/.config/tirith/policy.yaml
echo "✅ Tirith 策略已部署"

# 4. 部署铠甲 SKILL
mkdir -p ~/.hermes/skills/dogfood/hermes-armor/scripts
cp SKILL.md ~/.hermes/skills/dogfood/hermes-armor/SKILL.md 2>/dev/null || curl -fsSL https://raw.githubusercontent.com/ArtiNexus/hermes-armor/main/SKILL.md -o ~/.hermes/skills/dogfood/hermes-armor/SKILL.md
echo "✅ 铠甲 SKILL 已部署"

# 5. 部署门神脚本
cp gatekeeper.py ~/.hermes/skills/dogfood/hermes-armor/scripts/gatekeeper.py 2>/dev/null || curl -fsSL https://raw.githubusercontent.com/ArtiNexus/hermes-armor/main/gatekeeper.py -o ~/.hermes/skills/dogfood/hermes-armor/scripts/gatekeeper.py
chmod +x ~/.hermes/skills/dogfood/hermes-armor/scripts/gatekeeper.py
echo "✅ 门神脚本已部署"

# 6. 部署检查脚本
mkdir -p ~/.hermes/skills/dogfood/hermes-armor/scripts
cp scripts/post-update-check.sh ~/.hermes/skills/dogfood/hermes-armor/scripts/post-update-check.sh 2>/dev/null || curl -fsSL https://raw.githubusercontent.com/ArtiNexus/hermes-armor/main/scripts/post-update-check.sh -o ~/.hermes/skills/dogfood/hermes-armor/scripts/post-update-check.sh
chmod +x ~/.hermes/skills/dogfood/hermes-armor/scripts/post-update-check.sh
echo "✅ 检查脚本已部署"

# 7. 修改 config.yaml（tirith_fail_open）
if grep -q "tirith_fail_open:" ~/.hermes/config.yaml; then
  sed -i '' 's/tirith_fail_open: true/tirith_fail_open: false/' ~/.hermes/config.yaml 2>/dev/null || \
  sed -i 's/tirith_fail_open: true/tirith_fail_open: false/' ~/.hermes/config.yaml
  echo "✅ tirith_fail_open 已设为 false"
else
  echo "⚠️ 未找到 tirith_fail_open 配置，请手动添加"
fi

echo "=========================="
echo "✅ Hermes 铠甲安装完成！"
echo ""
echo "📋 下次启动 Hermes 时铠甲将自动加载"
echo "🔍 更新后检查: bash ~/.hermes/skills/dogfood/hermes-armor/scripts/post-update-check.sh"
echo "🔄 回滚: cp ~/.hermes/config.yaml.bak.hermes-armor ~/.hermes/config.yaml"
