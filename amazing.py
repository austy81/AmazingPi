import RPi.GPIO as GPIO
from pygame import mixer
import time
import os
import random
#from os import listdir
#from os.path import isfile, join

GPIO.setmode(GPIO.BOARD)
buttonPin = 3

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mixer.init()


script_path = os.path.dirname(os.path.realpath(__file__))
samples_dir = os.path.join(script_path,'samples')
audio_list = []

#  traverse samples directory and add all audio samples to list
for dir_name, subdir_list, file_list in os.walk(samples_dir):
    print('Found directory: %s' % dir_name)
    for file_name in file_list:
        if file_name.endswith(('.wav','.mp4')):
            print('\t%s' % file_name)
            audio_list.append(os.path.join(dir_name, file_name))

audio_file = random.choice(audio_list)
sound = mixer.Sound(audio_file)

prev_state = True
while True:
    current_state = GPIO.input(buttonPin)
    if (current_state == False) and (prev_state == True):
        sound.stop()
        audio_file = random.choice(audio_list)
        sound = mixer.Sound(audio_file)
        print('Playing %s' % audio_file)
        sound.play()
    prev_state = current_state
