#http://razzpisampler.oreilly.com/ch07.html
#Source: https://stackoverflow.com/questions/29289539/how-do-i-play-a-random-wav-sample-from-a-folder-in-python/29289595

import RPi.GPIO as GPIO
import os, random
import time, sys
from pygame import mixer

#Set up GPiO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Check for button press
while True:
    input_state = GPIO.input(17)
    if input_state == False:
        print('Button Pressed')

        #loop to get random track from file music
        def rndmp3():
            randomfile = random.choice(os.listdir("music"))
            file = randomfile
            print(file)

            #Initialize mixer and play randomly selected file from music folder
            mixer.init()

            sound = mixer.Sound("music/" + file)
            sound.play()

            #Time sound plays for
            time.sleep(5)

        rndmp3()
        
        time.sleep(0.2)
