順利以 pi 帳號登入之後的設定工作
# 從序列埠登入設定 WiFi
* [命令列設置無線網路](https://www.raspberrypi.com.tw/2152/setting-up-wifi-with-the-command-line/)
* [手動連接wifi](https://betaparticle.pixnet.net/blog/post/41609278)
# 語系及輸入法設定
![登入畫面](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/first_login.JPG)
pi@raspberry:~$ sudo raspi-config
![Raspi-config Menu](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/raspi-menu.JPG)
## 選擇： 4 Localisation Options
![Locale Menu](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/Locale_menu.JPG)
## 選擇：I1 Change Locale
![Locale Select](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/Locale_select.JPG)
## 按 PageDown 直到 zh_TW，以 [Space] 鍵選擇所有 zh_TW.**
## 按 <Tab> 選擇 [OK] 
## 往下選擇： zh_TW.UTF-8
#
## 再次進入 Localisation Options， 選擇 I2 Change Timezone
![Time Zone--Asia](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/Timezone_Asia.JPG)
## 選擇 Asia，選擇 Taipei，按 <Tab> 鍵，選擇 [OK]
![Asia/Taipei](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/Asia_Taipei.JPG)
## 再次進入 Localisation Options， 選擇 I4 Change Wi-fi Contry
![Wi-fi Contry](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/Wifi-contry.JPG)
## 選擇 TW Taiwan，按 <Tab> 鍵，選擇 [OK], 再次選擇 [OK]
#
# 接下來設定介面，由主選單選擇： Interface Options，然後將 SSH、VNC、I2C、Serial、Remote GPIO 打開
# 先不重開機
## 設定無線網路連接
#
# pi@raspberry:~$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
#
# 輸入 SSID、Key 如以下範例：
# 
### network={
###         ssid="netis_942253"
###         psk="12345678"
###         key_mgmt=WPA-PSK
### }
#
# 按 Ctrl-x 儲存後離開
# sync
# sync
# sync
# pi@raspberry:~$ sudo shutdown -r now     # sudo reboot
# 重開後看看網路是否有連結
# pi@raspberry:~$ hostname -I
# 如果有 IP，表示可以連上網路
#
# 更新套件
# pi@raspberry:~$ sudo apt-get update && sudo apt-get upgrade
# pi@raspberry:~$ sudo reboot
#
# 安裝輸入法及字型
#
# pi@raspberry:~$ sudo apt-get install scim-chewing
# pi@raspberry:~$ sudo apt-get install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy
#
# [參考網站](https://blog.gtwang.org/iot/raspberry-pi-chinese-input-method/)
  
