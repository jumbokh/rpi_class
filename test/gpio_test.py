import RPi.GPIO as GPIO
import time
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
# set up the GPIO channels - one input and one output
#GPIO.setup(11, GPIO.IN)
GPIO.setup(5, GPIO.OUT)
 
# input from pin 11
#input_value = GPIO.input(11)
 
# output to pin 12
for i in range(5):
    GPIO.output(5, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(5, GPIO.LOW)
    time.sleep(0.2)