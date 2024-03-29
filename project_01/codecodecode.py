"""
--------------------------------------------------------------------------
Code for Project 01 -- ENGI 301
--------------------------------------------------------------------------
License:   Copyright 2019 Bonnie Wang

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the 
following conditions are met:
    1. Redistributions of source code must retain the above copyright notice, this list of conditions and the 
    following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the 
    following disclaimer in the documentation and/or other materials provided with the distribution.
    3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote 
    products derived from this software without specific prior written permission.
    
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Software API:  
* update_flite
        - need to first install flite:
            apt-get install flite
* update_alsa-utils
--------------------------------------------------------------------------
Background Information:   
* Using text to speech commands with flite:    
    - http://einsteiniumstudios.com/make-your-beaglebone-speak.html
* (No base code)
--------------------------------------------------------------------------

"""

# Import required programs
import os system
import Adafruit_BBIO.EDC as ADC
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

# Global variables:
BUTTON = "P2_2"

# Initialize Button    
GPIO.setup(BUTTON, GPIO.IN)

# Initialize voice file
flite -t "this is the voice file" -o voicefile.wav

# When the button is pressed...
if(GPIO.input(BUTTON0) == 1):
    # Immediately start recording using the microphone for 10 seconds
    os.system(arecord -d 10 -f cd voicefile.wav)
    # Then will play the audio back from the audio output
    os.system(aplay voicefile.wav)

# That's it! (:
