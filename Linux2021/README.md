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
* 
## 2. 基本開發環境設定
### 1. 改 swap
* https://blog.gtwang.org/iot/raspberry-pi/raspberry-pi-swap-configuration-using-usb-stick/
* 設定 swap size 為 記憶體的 兩倍
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
#### 相關軟體安裝
<pre>
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera  -y
sudo apt-get install python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran  -y
sudo apt-get install libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp -y
sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev   -y
sudo apt-get install libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test  -y
sudo apt-get install python3-opencv -y
</pre>
##
#### 新建虛擬環境 env
<pre>
python3 -m virtualenv -p python3 env --system-site-packages
echo "source env/bin/activate" >> ~/.bashrc
source ~/.bashrc
</pre>
##
<pre>
python3 -m venv ds python=3.7
source ds/bin/activate
pip list
python -m pip install --upgrade pip
pip install numpy pandas matplotlib seaborn sklearn imageio 
pip install jupyter notebook
pip install opencv-python
python -c "import cv2"
sudo apt-get update && sudo apt-get install code
</pre>
##
### 5. Linux 基本指令 [常用 Linux 指令](https://ithelp.ithome.com.tw/articles/10235530)
* [Linux 目錄結構](https://iter01.com/561259.html) 
* [目錄結構 WiKi](http://linux-wiki.cn/wiki/zh-tw/Linux%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84)
* [使用者帳號與群組管理](http://120.105.184.250/peiyuli/unix/%E4%BD%BF%E7%94%A8%E8%80%85%E5%B8%B3%E8%99%9F%E8%88%87%E7%BE%A4%E7%B5%84%E7%AE%A1%E7%90%86.htm)
