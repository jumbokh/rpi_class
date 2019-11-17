## 設定語系、時區，參考: [first_time_setting](https://github.com/jumbokh/rpi_class/blob/master/Installation/first_time_setting.md)
* sudo raspi-config
* sudo reboot
## 設定無線網路
* ifconfig
* sudo vi /etc/wpa_supplicant/wpa_supplicant.conf 
### 貼上以下內容

* network={
*   ssid="TP-LINK_940"
*   psk="12345678"
*   key_mgmt=WPA-PSK
* }

###
* sudo reboot
###
* sudo apt-get update
* sudo apt-get install wget git tree
* sudo apt-get upgrade
* sudo reboot
### 安裝開發環境
* python --version
* python3 --version
* sudo apt purge timidity lxmusic gnome-disk-utility deluge-gtk evince wicd wicd-gtk clipit usermode gucharmap gnome-system-tools pavucontrol
* sudo apt-get install python-rpi.gpio python3-rpi.gpio
* mkdir src
* git clone https://github.com/jumbokh/rpi_class
### 安裝視窗環境
* sudo apt-get install xrdp
* ip addr
* sudo apt-get install lxde-core lxappearance
* sudo apt-get install xfce4 xfce4-terminal
* sudo apt-get install mate-desktop-environment-core
* sudo apt-get install lightdm
* sudo reboot
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
* sudo apt-get update
* sudo apt-get install chromium-browser
* sudo apt-get install python3-thonny
###
### 安裝完整開發環境
* pip3 install numpy matplotlib
* sudo apt-get install build-essential cmake unzip pkg-config
* sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
* sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
* sudo apt-get install libxvidcore-dev libx264-dev
* sudo apt-get install libgtk-3-dev
* sudo apt-get install libatlas-base-dev gfortran
* wget https://bootstrap.pypa.io/get-pip.py
* sudo python3 get-pip.py
* sudo pip install virtualenv virtualenvwrapper
* sudo rm -rf ~/get-pip.py ~/.cache/pip
* vi .bashrc
### 貼上以下資料
* \# virtualenv and virtualenvwrapper
* export WORKON_HOME=$HOME/.virtualenvs
* export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
* source /usr/local/bin/virtualenvwrapper.sh
###

source ~/.bashrc
### 建立虛擬環境
* mkvirtualenv cv -p python3
* cd ~
* git clone https://github.com/jumbokh/rpi_class
* workon cv
* pip3 install -r rpi_class/lite_install/require.txt
* sudo vi /etc/dphys-swapfile 
* sudo /etc/init.d/dphys-swapfile stop
* sudo /etc/init.d/dphys-swapfile start
* swapon -s
### 設定 jupyter notebook

jupyter notebook --generate-config

### 修改 ~/.jupyter/jupyter_notebook_config.py 找到
### \#c.NotebookApp.ip = ‘localhost'

### 改成

### c.NotebookApp.ip = '0.0.0.0’ 
### \# 設定瀏覽器登入 jupyter notebook server密碼
jupyter notebook password
### jupyter notebook --ip=192.168.x.x --no-browser
### 在本地端電腦瀏覽器，輸入:
http://192.168.x.x:
###
### 安裝 docker
* curl -sSL https://get.docker.com | sh
* sudo usermod -aG docker pi
* docker images
* docker login
* sudo docker pull howardweng/howard-node-red-lass
* docker version
* sudo docker images
* sudo docker ps
* sudo docker run -it -p 1880:2222 howardweng/howard-node-red-lass
