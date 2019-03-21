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
#
##### 燒錄系統至 SD卡
#
* config.txt 於檔案最後加以下3行：
* dtoverlay=pi3-miniuart-bt
* core_freq=250
* enable_uart=1
#
##### cmdline.txt 修改成：
* dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 root=PARTUUID=22dedadf-02 rootfstype=ext4 elevator=deadline 
* fsck.repair=yes rootwait splash plymouth.ignore-serial-consoles
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
