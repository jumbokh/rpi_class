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
## 1. Linux 安裝及樹莓派的初始設定
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

##### WiFi Not working
* sudo nano /etc/network/interface.d/wlan0
##### 貼上以下內容, 修改 ssid,key 儲存後重新開機
<pre>
allow-hotplug wlan0
iface wlan0 inet dhcp
    wpa-ssid your-ssid
    wpa-psk your-key
</pre>
##
#### 尋找樹莓派 ip 方法:
* 1. I2C oled ![OLED](https://github.com/jumbokh/rpi_class/blob/master/Linux2021/oled.JPG)
*    ![RPi4](https://github.com/jumbokh/rpi_class/blob/master/Linux2021/rpi4.JPG)
*    軟體:
<pre>
git clone https://github.com/waveshare/pi-display
cd pi-display
sudo ./install.sh
</pre>
![oled-i2c](https://github.com/jumbokh/rpi_class/blob/master/Linux2021/oled-i2c.jpg)
##
* 2. Angry IP scanner [官網](https://angryip.org/)
* ![scan ip](https://github.com/jumbokh/rpi_class/blob/master/Linux2021/ip-scan.JPG)
##
* 3. [IOS: Network Analyzer](https://apps.apple.com/tw/app/network-analyzer/id562315041)
     [Android](https://play.google.com/store/apps/details?id=net.techet.netanalyzerlite.an&hl=zh_TW&gl=US)
     ![Network Analyzer](https://github.com/jumbokh/rpi_class/blob/master/Linux2021/net-ana.jpg)
##
## 2. 基本開發環境設定
### 1. 改 swap
* https://blog.gtwang.org/iot/raspberry-pi/raspberry-pi-swap-configuration-using-usb-stick/
* 設定 swap size 為 記憶體的 兩倍
##
### 安裝開發環境
* python --version
* python3 --version
* sudo apt purge timidity lxmusic gnome-disk-utility deluge-gtk evince wicd wicd-gtk clipit usermode gucharmap gnome-system-tools pavucontrol
* sudo apt-get install python-rpi.gpio python3-rpi.gpio
* sudo apt install python3-opencv
* mkdir src
* git clone https://github.com/jumbokh/rpi_class
### 安裝視窗環境
* sudo apt-get install xrdp
* ip addr
* sudo apt-get install lxde-core lxappearance
* sudo apt-get install xfce4 xfce4-terminal
* sudo apt-get install mate-desktop-environment-core
* sudo apt-get install lightdm
* sudo apt-get install scim-chewing
* sudo apt-get install ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy
* cp /etc/X11/xinit/xinitrc ~/.xinitrc
* vi ~/.xinitrc
###### 貼上下面這一行
exec openbox-session
###

* sudo apt-get install rc-gui
* sudo apt-get install openbox lxterminal
* sudo apt-get install lightdm
* sudo reboot
##
### 測試 X-Window
* Step 1. 取得 ip 位址
* Step 2. New 一個 MobaXterm Session
    * 選擇 ssh
    * Advanced SSH Settings -> Remote Environment: Xfce4 desktop
    * 登入, 等候畫面啟動
* 解決遠端桌面的中文輸入法: [樹莓派 RaspBerry Pi 中文輸入法 (新酷音輸入法)](https://books.bod.idv.tw/2019/07/raspberry-pi.html)
##
### 2. 安裝開發環境
* https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E4%B8%80%E3%80%81Raspberry_Pi%E5%AE%89%E8%A3%85
### 3. 設定 python3 為 default python [參考](https://linuxconfig.org/change-default-python-version-on-raspbian-gnu-linuxl)
* Step 1. Add both (all) versions of python installed to the list of "alternatives" for the python binary.
<pre>
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 2
</pre>
* Step 2. Select desired version:
<pre>
sudo update-alternatives --config python
</pre>
### 4. 設定 virtual env, and install packages
* 參考: [Donkey Car 環境設定](https://www.waveshare.net/wiki/DonkeyCar_for_PiRacer_Pro_%E6%95%99%E7%A8%8B%E4%B8%80%E3%80%81Raspberry_Pi%E5%AE%89%E8%A3%85)
#### 相關軟體安裝 ( 參考: [Install OpenCV 4 on Raspberry Pi 4 and Raspbian Buster](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) )
<pre>
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera  -y
sudo apt-get install python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran  -y
sudo apt-get install libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp -y
sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev   -y
sudo apt-get install libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test  -y
sudo apt-get install python3-opencv -y
sudo apt-get install cmake pkg-config libjpeg-dev libpng-dev libavcodec-dev libavformat-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev -y
sudo apt-get install libgtk2.0-dev libgtk-3-dev libatlas-base-dev -y
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103 -y
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 -y
sudo apt-get install python3-dev -y
</pre>
##
#### install pip
<pre>
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo python3 get-pip.py
$ sudo rm -rf ~/.cache/pip
</pre>
##
#### 遠端桌面連線
* sudo apt-get install xrdp
* 在 win10 上執行遠端桌面連線 (可以調整選項, 以免佔用全部螢幕)
#### 新建虛擬環境 env
<pre>
python3 -m virtualenv -p python3 env --system-site-packages
echo "source env/bin/activate" >> ~/.bashrc
source ~/.bashrc
deactivate # 離開虛擬環境
</pre>
##
<pre>
python3 -m venv ds python=3.7
source ds/bin/activate
pip list
python -m pip install --upgrade pip
pip install numpy pandas matplotlib seaborn scipy sklearn imageio 
pip install jupyter notebook
pip install opencv-python
python -c "import cv2"
sudo apt-get update && sudo apt-get install code
</pre>
##
### 5. Linux 基本指令
* pwd, cd, ls
    * ls -l : long list
    * ls -al : 顯示隱藏檔案 (以 "." 開頭的目錄或檔名)
* 權限 rwx
##### -rwxr--r-- 1 jumbo jumbo 51  7月  3 21:23 jlab.sh
* 第一個 "-" : 代表一般檔 (ordinary file)
* "d" : 目錄
* "c" : character special device (字符特殊檔案設備)
* "b" : block special device (區塊特殊檔案設備)
* "F" : FIFO special device (first in first out 特殊檔案設備)
* "l" : link, 捷徑, 連結至指定檔案或目錄
##
#### 接下來的字元 以三個為一組 rwx (4,2,1), 分別限定 所有權人(創建人), 群組成員, 其他成員 的權限
#### 比如:
* -rwxr--r-- 1 jumbo jumbo 51  7月  3 21:23 jlab.sh
    * 為一般檔案, (但是為 shell script file)
    * 擁有者 jumbo: 可讀 可寫 可執行
    * 群組 jumbo:可讀
    * 其他: 可讀
    * 最後更新時間: 7/3 21:23
* 修改權限: chmod
    * 如: chmod 644 jlab.sh
    * -rw-r--r-- 1 jumbo jumbo 51  7月  3 21:23 jlab.sh
        * 擁有者 jumbo: 可讀 可寫  
        * 群組 jumbo:可讀 
        * 其他: 可讀 
    * * 如: chmod 777 jlab.sh #(警告: 儘量不要設定此類權限, 易造成系統漏洞)
    * -rwxrwxrwx 1 jumbo jumbo 51  7月  3 21:23 jlab.sh
        * 擁有者 jumbo: 可讀 可寫 可執行 
        * 群組 jumbo:可讀 可寫 可執行
        * 其他: 可讀 可寫 可執行
***
* touch file-name
    * file-name 不存在: 新建檔案, 檔名 file-name
    * file-name 存在: 更新最後修改時間為現在
***
#### 相關說明參考 [鳥站](https://linux.vbird.org/linux_basic/redhat6.1/linux_06command.php)
* find / -name "cv.*" -print
* cat ~/.bashrc | grep PATH
* ifconfig | grep inet
* ps -aux 
* kill -9 process-id
* ln -fs source target
* whereis && which
#### 備份 & cron job [鳥站](http://linux.vbird.org/linux_basic/0580backup.php)
* 備份目錄:
    * /etc
    * /var/lib/mysql
    * /var/www/html
    * /home
    * /boot
* 寫一 backupday.sh 進行每日備份
* 執行: sudo crontab -e
       * 於最後一行加上: 分 時 日期 月份 週 指令 #### 見: [鳥站](http://linux.vbird.org/linux_basic/0430cron.php)
       * 如: 59 23 * * * /usr/local/bin/backupday.sh > /dev/null 2>&1
##
* [dnstuils](https://www.tecmint.com/install-dig-and-nslookup-in-linux/)
* [dig](https://ithelp.ithome.com.tw/articles/10214466)
* [DNS](https://www.myfreax.com/how-to-use-dig-command-to-query-dns-in-linux/)
* [DNS-1](https://haway.30cm.gg/dns-4-dig/)
* [dig](https://www.azureunali.com/linuxnetwork-dig%E6%8C%87%E4%BB%A4%E7%B4%80%E9%8C%84/)
* #### dig @dns.hinet.net A gigaenergy.com.tw
* #### dig @dns.hinet.net MX gigaenergy.com.tw
* ####  dig +nocmd tecadmin.net ALL +noall +answer
***
### 參考
* [常用 Linux 指令](https://ithelp.ithome.com.tw/articles/10235530)
* [鳥哥的 Linux 指令介紹](https://linux.vbird.org/linux_basic/redhat6.1/linux_06command.php)
* [Linux 目錄結構](https://iter01.com/561259.html) 
* [目錄結構 WiKi](http://linux-wiki.cn/wiki/zh-tw/Linux%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84)
* [使用者帳號與群組管理](http://120.105.184.250/peiyuli/unix/%E4%BD%BF%E7%94%A8%E8%80%85%E5%B8%B3%E8%99%9F%E8%88%87%E7%BE%A4%E7%B5%84%E7%AE%A1%E7%90%86.htm)
* [Unix 演進圖](https://zh.wikipedia.org/wiki/UNIX#/media/File:Unix_history-simple.svg)
* [Build opencv 4.4.0](https://qengineering.eu/install-opencv-4.4-on-raspberry-pi-4.html)
* [安裝 pytorch](https://zhuanlan.zhihu.com/p/79807661)
* [安裝 Wordpress](https://behind-the-scenes.net/installing-wordpress-on-a-raspberry-pi-raspbian/)
