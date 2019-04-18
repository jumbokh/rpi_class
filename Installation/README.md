## 樹莓派安裝
#
#### 工具程式及系統：
* 1. [SD Formater](https://www.sdcard.org/downloads/formatter_4/)
#
![image](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/sdformater.JPG)
#
* 2. [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/)
#
![image](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/win32diskimager.JPG)
#
* 3. [putty 終端機程式](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
* 4. [作業系統](https://www.raspberrypi.org/downloads/)
* 5. [無線網路監控](https://briian.com/8293/)
#
* [下載線](https://goods.ruten.com.tw/item/show?21614419065751)
* [USB-TTL](https://goods.ruten.com.tw/item/show?21618647811364)
### [安裝請參考:28頁](https://github.com/jumbokh/rpi_class/blob/master/NCTU/IoT%20platform%20course(Raspberry%20Pi)%20(2).pdf)
![usb-ttl](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/USB_TTL.jpg)
![connect to serial](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/connect-serial-to-raspberry-pi-model-b-plus.png)
#
##### 燒錄系統至 SD卡
#
##### config.txt 於檔案最後加以下3行：
* dtoverlay=pi3-miniuart-bt
* core_freq=250
* enable_uart=1
#
##### cmdline.txt 修改成：
* dwc_otg.lpm_enable=0 console=tty1 console=serial0,115200 root=PARTUUID=4c34f55a--02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait splash plymouth.igg nore-serial-consoles
#
* [refers](https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3/)
##### 放一個空的檔案： SSH 至根目錄下 (SD卡目錄最頂端)
#
##### 接下來把 USB-TTL 線連接至樹莓派，先不連接電腦
#
##### 連接樹莓派電源，開啟 [無線網路監控程式](https://briian.com/8293/)
#
##### 執行 putty 連接
#
##### [關掉藍芽](https://blog.sleeplessbeastie.eu/2018/12/31/how-to-disable-onboard-wifi-and-bluetooth-on-raspberry-pi-3/) 
* $ echo "dtoverlay=pi3-disable-bt" | sudo tee -a /boot/config.txt
* $ sudo systemctl disable hciuart
* $ sudo reboot
# [overlays](https://github.com/raspberrypi/firmware/blob/master/boot/overlays/README)

# 無線網路設定
#
* sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
* network={
*        ssid="netis_942253"
*        psk="12345678"
*        key_mgmt=WPA-PSK
* }
## $ sudo ifconfig
![wlan config](https://github.com/jumbokh/rpi_class/blob/master/Installation/wlan0.JPG)
