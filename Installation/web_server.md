## Step 1 更新 Raspberry pi 韌體
* sudo apt-get install ca-certificates
* sudo apt-get install git-core
* sudo wget http://goo.gl/1BQfJ -O /usr/bin/rpi-update && sudo chmod +x /usr/bin/rpi-update
* sudo rpi-update
* sudo shutdown -r now
#
## Step 2 更新 apt-get
* sudo apt-get update
* sudo apt-get upgrade
#
## Step 3 安裝網頁伺服器 apache2
* sudo apt-get install apache2
#
## Step 4 安裝 PHP 程式語言
* sudo apt-get install php5 libapache2-mod-php5
#
## Step 5 重新啟動 web Server
* sudo service apache2 restart
#
## Step 6 確認 Raspberry Pi 的 ip 位置
* ifconfig
![ip address]()
#
## Step 7 透過網路瀏覽來測試
* ping dns.hinet.net
## 或是瀏覽器輸入 Raspberry Pi ip 位址，如：192.168.0.4
