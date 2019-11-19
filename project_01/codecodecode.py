import os system
import Adafruit_BBIO.EDC as ADC
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

BUTTON = "P2_2"
#Initialize Button    
GPIO.setup(BUTTON, GPIO.IN)
#Initialize voice file
flite -t "this is the voice file" -o voicefile.wav

if(GPIO.input(BUTTON0) == 1):
    os.system(arecord -d 10 -f cd voicefile.wav)
    os.system(aplay voicefile.wav)
