下面是可直接複製的 Windows PowerShell 指令清單。
請先把這一行中的路徑改成你自己的使用者名稱：

$VAULT="C:\Users\你的帳號\Documents\Obsidian\OpenClawVault"


---

# =========================================
# OpenClaw + Obsidian（Windows）安裝與測試指令清單
# 請在 PowerShell 執行
# =========================================

# 0. 設定你的 Obsidian Vault 路徑
$VAULT="C:\Users\你的帳號\Documents\Obsidian\OpenClawVault"

# 1. 建立 Vault 資料夾與基本結構
New-Item -ItemType Directory -Force -Path $VAULT
New-Item -ItemType Directory -Force -Path "$VAULT\Inbox"
New-Item -ItemType Directory -Force -Path "$VAULT\Daily"
New-Item -ItemType Directory -Force -Path "$VAULT\Projects"
New-Item -ItemType Directory -Force -Path "$VAULT\Templates"

# 2. 安裝 OpenClaw（PowerShell）
iwr -useb https://openclaw.ai/install.ps1 | iex

# 3. 安裝 / 設定 OpenClaw daemon
openclaw onboard --install-daemon

# 4. 檢查 OpenClaw 是否安裝成功
openclaw --version

# 5. 檢查 Obsidian CLI 是否可用
# 注意：
# 你必須先手動完成這兩件事：
# (1) 已安裝 Obsidian 桌面版
# (2) 在 Obsidian -> Settings -> General -> Enable CLI 開啟
# (3) Obsidian 程式目前必須正在執行中
obsidian version
obsidian help

# 6. 手動建立一個測試筆記
"# OpenClaw Test`n這是一份測試筆記。" | Out-File -Encoding utf8 "$VAULT\Inbox\test-note.md"

# 7. 查看目前 vault 資訊
obsidian vault
obsidian vault info=path

# 8. 讀取今日 Daily Note
# 若尚未建立，某些版本可能會提示不存在
obsidian daily:read

# 9. 搜尋 vault 中的關鍵字
obsidian search query="OpenClaw"
obsidian search query="test"

# 10. 建立今天的 Daily Note（若不存在）
$today = Get-Date -Format "yyyy-MM-dd"
"# $today`n`n- 今日測試 OpenClaw + Obsidian" | Out-File -Encoding utf8 "$VAULT\Daily\$today.md"

# 11. 再次讀取 Daily Note
obsidian daily:read

# 12. 追加內容到 Daily Note
Add-Content -Encoding utf8 "$VAULT\Daily\$today.md" "`n- 第二筆測試內容"

# 13. 建立專案筆記
@"
# Project Test

## Goal
測試 OpenClaw 與 Obsidian 整合

## Tasks
- [ ] 安裝 OpenClaw
- [ ] 啟用 Obsidian CLI
- [ ] 測試搜尋
- [ ] 測試 Daily Note
"@ | Out-File -Encoding utf8 "$VAULT\Projects\project-test.md"

# 14. 再搜尋一次專案筆記內容
obsidian search query="Project Test"
obsidian search query="測試 OpenClaw 與 Obsidian 整合"

# 15. 顯示剛建立的檔案清單
Get-ChildItem -Recurse $VAULT

# 16. 用 Obsidian 開啟 vault
# 某些版本可直接接受 vault 路徑；若不行，就先手動在 Obsidian 開啟該資料夾
obsidian open "$VAULT"


---

你還需要手動做的事

這些不是 PowerShell 指令，但一定要先完成：

1. 先安裝 Obsidian Windows 桌面版


2. 打開 Obsidian


3. 到 Settings → General


4. 開啟 Enable CLI


5. 保持 Obsidian 正在執行


6. 手動開啟你的 vault 資料夾一次




---

最小測試版本

如果你只想先跑最核心的幾條，先複製這段：

$VAULT="C:\Users\你的帳號\Documents\Obsidian\OpenClawVault"
New-Item -ItemType Directory -Force -Path "$VAULT\Inbox"
iwr -useb https://openclaw.ai/install.ps1 | iex
openclaw onboard --install-daemon
openclaw --version
obsidian version
obsidian vault
"# test" | Out-File -Encoding utf8 "$VAULT\Inbox\test.md"
obsidian search query="test"

如果你要，我下一則可以直接幫你補一份 .ps1 可執行腳本版。