import RPi.GPIO as GPIO
from pygame import mixer
import time

GPIO.setmode(GPIO.BOARD)
buttonPin = 3

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mixer.init()
sound = mixer.Sound('samples/test.wav')

prev_state = True
while True:
    current_state = GPIO.input(buttonPin)
    if (current_state == False) and (prev_state == True):
        sound.stop()
        print('Playing...')
        sound.play()
    prev_state = current_state