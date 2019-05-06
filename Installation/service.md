### Samba server 檔案分享
#### 參考：[Samba 伺服器](http://yehnan.blogspot.com/2016/05/raspberry-pisamba.html)
## 安裝
#
* sudo apt-get install samba
* sudo usermod -a -G sambashare pi
#
## 修改設定檔：
* sudo nano /etc/samba/smb.conf
### 在最後加入
* [pi]
* comment=pi's home
* path=/home/pi
* read only=no
* guest ok=no
* browseable=yes
* create mask=0750
* directory mask=0750
#
* sudo /etc/init.d/samba restart
#
## 連接網路磁碟機
## 假設樹莓派的 ip 為： 192.168.0.4
### windows:
* \\192.168.0.4
### Linux:
* smb://192.168.1.16/pi
