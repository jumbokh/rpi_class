### 樹莓派腳位定義: source:[Raspberry Pi 2 & 3 個 Pin 對應](https://docs.microsoft.com/zh-tw/windows/iot-core/learn-about-hardware/pinmappings/pinmappingsrpi)
![樹莓派腳位](rp2_pinout.png)
#
<pre>
在 Python 中設定GPIO.BOARD與GPIO.BCM有何不同

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

或者

GPIO.setmode(GPIO.BCM)

這個GPIO.BOARD 選項是指定在電路版上接脚的號碼
這個GPIO.BCM 選項是指定GPIO後面的號碼
在撰寫程式時要先清楚你指定的數字要使用的是GPIO.BOARD或是GPIO.BCM的方式
</pre>
##
[程式:gpio_bcm.py](gpio_bcm.py)
### 必要模組:
* pip3 install RPi.GPIO
### 執行:
* sudo python3 gpio_bcm.py
##
![LED接線](RPi_LED_bb.jpg)
* [A People Counter with Raspberry Pi and Ubidots](https://www.hackster.io/ubimaker/a-people-counter-with-raspberry-pi-and-ubidots-2b53be)
