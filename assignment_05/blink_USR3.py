import Adafruit_BBIO.GPIO as GPIO
import time

for i in range(4);
  GPIO.setup("USR%d" % i, GPIO.OUT)
  
while True:
  GPIO.output("USR3", GPIO.HIGH)
  time.sleep(0.1)
  GPIO.output("USR3", GPIO.LOW)
  time.sleep(0.1)
