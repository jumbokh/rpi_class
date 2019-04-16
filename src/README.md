### GPIO 基礎實驗
* 開始前的準備步驟
###### 1. sudo raspi-config
######     啟用 interfaceing option->remote GPIO Control
* 準備 python3.6 虛擬環境
* 1. sudo su -
* 2. $ sudo rpi-update
*    $ sudo apt-get update
*    $ sudo apt-get upgrade
*    $ sudo reboot
* 3. $ sudo apt-get install build-essential git cmake pkg-config
* 4. $ sudo apt-get install python-setuptools
* 5. $ sudo apt-get install virtualenv virtualenvwrapper
* 6. $ sudo su -
*     \# virtualenv py36 -p python3.6
*     \# source py36/bin/activate
*     (py36)\# pip install numpy
*     (py36)\# sudo apt-get install libblas-dev 
*     (py36)\# sudo apt-get install liblapack-dev      
*     (py36)\# [sudo apt-get install python-dev        ## Optional]
*     (py36)\# [sudo apt-get install libatlas-base-dev ## Optional speed up execution]
*     (py36)\# sudo apt-get install gfortran           
*     (py36)\# sudo apt-get install python-setuptools  
*     (py36)\# sudo easy_install scipy                 
*     (py36)\# ## previous might also work: python-scipy without all dependencancies
*     (py36)\# sudo apt-get install python-matplotlib  
*     (py36)\# sudo apt-get install python3-rpi.gpio
*     (py36)\# sudo apt-get install python-rpi.gpio
*     (py36)\# pip3 install RPi.GPIO
*     (py36)\# apt-get install python3-gpiozero
*     (py36)\# pip3 install gpiozero
#
## Matplotlib 的 example 如下:
#
### import matplotlib.pyplot as plt
### plt.plot([1,2,3,4])
### plt.ylabel('some numbers')
### plt.show()
#
# [matplotlib examples](https://matplotlib.org/1.4.1/users/pyplot_tutorial.html)
#
### 腳位圖
![GPIO pinout](https://github.com/jumbokh/rpi_class/blob/master/src/images/166109.jpg)
![溫溼度感測器 DHT11接線圖](https://github.com/jumbokh/rpi_class/blob/master/src/images/166107.jpg)
![LED 接線圖](https://github.com/jumbokh/rpi_class/blob/master/src/images/166108.jpg)

