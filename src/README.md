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
* 4. $ sudo pip install virtualenv virtualenvwrapper
* 5. $ sudo su -
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
## Matplotlib 的 example 如下:
#
### import matplotlib.pyplot as plt
### plt.plot([1,2,3,4])
### plt.ylabel('some numbers')
### plt.show()
#
# [matplotlib examples](https://matplotlib.org/1.4.1/users/pyplot_tutorial.html)

