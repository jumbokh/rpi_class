![GPIO 腳位](https://github.com/jumbokh/rpi_class/blob/master/Installation/image/Pi2%20GPIO.png)
### GPIO 基礎實驗
* 開始前的準備步驟
###### 1. sudo raspi-config
######     啟用 interfaceing option->remote GPIO Control
* 準備 python3.5 虛擬環境
* 1. sudo su -
* 2. $ sudo rpi-update
*    $ sudo apt-get update
*    $ sudo apt-get upgrade
*    $ sudo reboot
* 3. $ sudo apt-get install build-essential git cmake pkg-config
* 4. $ sudo apt-get install python-setuptools
* 5. $ sudo apt-get install virtualenv virtualenvwrapper
* 6. $ sudo su -
*    # virtualenv py3 -p python3.5
*    # source py3/bin/activate
*     (py3)\# pip install numpy
*     (py3)\# sudo apt-get install libblas-dev 
*     (py3)\# sudo apt-get install liblapack-dev      
*     (py3)\# sudo apt-get install python3-dev        ## Optional
*     (py3)\# sudo apt-get install libatlas-base-dev ## Optional speed up execution
*     (py3)\# sudo apt-get install gfortran           
*     (py3)\# sudo apt-get install python-setuptools  
*     (py3)\# sudo apt-get install python3-rpi.gpio
*     (py3)\# sudo apt-get install python-rpi.gpio
*     (py3)\# pip3 install RPi.GPIO
*     (py3)\# apt-get install python3-gpiozero
*     (py3)\# pip3 install gpiozero
*     (py3)\# pip3 install jupyter
*     (py3)\# ifconfig
## Lab Start here
*     (py3)\# mkdir source
*     (py3)\# cd source
*     (py3)\# git clone https://github.com/jumbokh/rpi_class
*     (py3)\# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
*     (py3)\# cd Adafruit_Python_DHT
*     (py3)\# python setup.py install
*     (py3)\# cd ..
*     (py3)\# pip install environment_kernels
*     (py3)\# jupyter notebook --generate-config
*     (py3)\# jupyter notebook --ip=192.168.1.111 --no-browser --allow-root 
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

