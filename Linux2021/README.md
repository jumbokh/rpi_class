### Linux 課程 (以樹莓派)
##
### 課程計畫
* 1. Linux 安裝及樹莓派的初始設定
* 2. 基本 Unix 指令
* 3. 開關機及檔案目錄權限與操作
* 4. 排程備份與檔案壓縮
* 5. 網路設定與寬頻上網
* 6. 文書編輯
* 7.  網路工具
* 8. 防火牆與 VNC
* 9. 系統管理基礎, syslog, 清檔
* 10. SHELL 簡介
* 11. 架設 WWW 伺服器
* 12. 架設 FTP 伺服器
* 13. Mail Server
* 14. Samba Server
* 15. DNS server
* 16. DHCP Server
* 17. NAT Server
* 18. Docker
* 19 Node-red 課程(暫定)
* 20 系統救援
##
##### 1. Linux 安裝及樹莓派的初始設定
## 無螢幕、鍵盤滑鼠, 安裝步驟
* Step 1. 下載 作業系統映像檔 [Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/)
    * 請選擇: Raspberry Pi OS with desktop and recommended software
* Step 2. 燒錄映像檔至 SD卡
    * 下載安裝 [etcher]( https://www.balena.io/etcher/)
    * 燒錄剛剛下載之映像檔(請解壓縮)
* Step 3. 允許透過 ssh 登入系統
    * 在剛剛燒錄完成的 sd卡中建立一個空檔: ssh (請注意無附屬檔名)
* Step 4. 添加 wifi 資訊
    * 在 sd 卡上建立 wpa_supplicant.conf 檔案 (宜使用 nodepad++編輯)
    * 檔案內容, 如下:
##
<pre>
country=TW
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
</pre>
##
* Step 5. 退出 sd 卡
* Step 6. 將sd卡插入樹莓派, 開啟電源
* 
