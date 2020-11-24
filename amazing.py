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


script_path = os.path.dirname(os.path.realpath(__file__))
samples_dir = os.path.join(script_path,'samples')
samples_list = []
wav = os.path.join(samples_dir,'test.wav')

#  traverse samples directory and add all audio samples to list
for dir_name, subdir_list, file_list in os.walk(samples_dir):
    print('Found directory: %s' % dir_name)
    for file_name in file_list:
        if file_name.endswith(('.wav','.mp4')):
            print('\t%s' % file_name)
            samples_list.append(os.path.join(dir_name, file_name))

sound = mixer.Sound(wav)

prev_state = True
while True:
    current_state = GPIO.input(buttonPin)
    if (current_state == False) and (prev_state == True):
        sound.stop()
        print('Playing...')
        sound.play()
    prev_state = current_state
