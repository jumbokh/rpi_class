## Installing Python3.6 on a Raspberry Pi
* sudo apt-get install python3-dev libffi-dev libssl-dev -y
* sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev
* wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
* tar xJf Python-3.6.3.tar.xz
* cd Python-3.6.3
* ./configure
* make
* sudo make install
* sudo pip3 install --upgrade pip
## 先看一下python3和python命令分别在那
* pi@raspberrypi:~ $ which python
* /usr/bin/python
* pi@raspberrypi:~ $ which python3
* /usr/local/bin/python3
## 重新建立連結
* pi@raspberrypi:~ $ sudo mv /usr/bin/python /usr/bin/python2.7.2
##
* pi@raspberrypi:~ $ sudo ln -s /usr/local/bin/python3 /usr/bin/python
## 测试是否成功
* pi@raspberrypi:~ $ python --version
#
* Python 3.6.1
