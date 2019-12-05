import RPi.GPIO as GPIO
from time import sleep

# the same script as above but using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(2, GPIO.IN)
GPIO.setup(2, GPIO.OUT)
#input_value = GPIO.input(17)
for i in range(5):
    GPIO.output(2, GPIO.HIGH)
    sleep(1)
    GPIO.output(2, GPIO.LOW)
    sleep(1)
