# 先檢查一下更新
sudo apt update
# 安裝 ifconfig
sudo apt install net-tools
# 安裝 iwconfig
sudo apt install wireless-tools
# 安裝 wpasupplicant
sudo apt install wpasupplicant
wpa_passphrase "你的WIFI名稱" "你的WIFI密碼"| sudo tee /etc/wpa_supplicant.conf
sudo wpa_supplicant -c /etc/wpa_supplicant.conf -i wlan0
# 正確的結果，大概長這樣
Successfully initialized wpa_supplicant
wlan0: Trying to associate with SSID 'TEST-WIFI'
wlan0: Associated with c5:4a:21:53:ac:eb
wlan0: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlan0: WPA: Key negotiation completed with c5:4a:21:53:ac:eb
[PTK=CCMP GTK=TKIP]wlan0: CTRL-EVENT-CONNECTED - Connection to c5:4a:21:53:ac:eb completed [id=0 id_str=]
sudo wpa_supplicant -B -c /etc/wpa_supplicant.conf -i wlan0
sudo dhclient wlan0
# 先搬設定檔
sudo cp /lib/systemd/system/wpa_supplicant.service /etc/systemd/system/wpa_supplicant.service

# 修改設定檔
# 不會用vim的同學可以用自己常用的沒關係
sudo vim /etc/systemd/system/wpa_supplicant.service

找到這行：
ExecStart=/sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
把它改成這樣
ExecStart=/sbin/wpa_supplicant -u -s -c /etc/wpa_supplicant.conf -i wlan0
sudo vim /etc/systemd/system/dhclient.service

貼上以下內容然後保存

[Unit]
Description= DHCP Client
Before=network.target
After=wpa_supplicant.service
[Service]
Type=simple
ExecStart=/sbin/dhclient wlan0
[Install]
WantedBy=multi-user.target
之後啟動服務

sudo systemctl enable dhclient.service
