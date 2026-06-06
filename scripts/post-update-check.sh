#!/bin/bash
# 🛡️ Hermes 铠甲 — Hermes 更新后检查脚本
# 用法: bash post-update-check.sh
# 功能: 检查 Hermes 更新后关键配置是否被覆盖

echo "🔍 Hermes 铠甲 — 更新后配置检查"
echo "================================"

FAIL=0

# 检查 tirith_fail_open
if grep -q "tirith_fail_open: false" ~/.hermes/config.yaml 2>/dev/null; then
  echo "✅ tirith_fail_open: false — 正确"
else
  echo "❌ tirith_fail_open 被重置！需要修改为 false"
  FAIL=1
fi

# 检查 Tirith 策略文件
if [ -f ~/.config/tirith/policy.yaml ]; then
  echo "✅ Tirith 策略文件存在"
else
  echo "❌ Tirith 策略文件缺失！需要重新部署"
  FAIL=1
fi

# 检查铠甲 SKILL 是否存在
if [ -f ~/.hermes/skills/dogfood/hermes-armor/SKILL.md ]; then
  echo "✅ 铠甲 SKILL 存在"
else
  echo "❌ 铠甲 SKILL 缺失！需要重新安装"
  FAIL=1
fi

# 检查 Tirith 二进制
if [ -f ~/.hermes/bin/tirith ]; then
  echo "✅ Tirith 二进制存在"
else
  echo "⚠️ Tirith 二进制未找到，Hermes 会自动安装"
fi

echo "================================"
if [ $FAIL -eq 0 ]; then
  echo "✅ 一切正常，铠甲运行中"
else
  echo "⚠️ 发现配置异常，请重新运行安装脚本"
fi
