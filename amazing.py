import RPi.GPIO as GPIO
from pygame import mixer
import time
import os
#from os import listdir
#from os.path import isfile, join

GPIO.setmode(GPIO.BOARD)
buttonPin = 3

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mixer.init()


full_path = os.path.dirname(os.path.realpath(__file__))
wav = os.path.join(full_path,'samples','test.wav')

sound = mixer.Sound(wav)

prev_state = True
while True:
    current_state = GPIO.input(buttonPin)
    if (current_state == False) and (prev_state == True):
        sound.stop()
        print('Playing...')
        sound.play()
    prev_state = current_state