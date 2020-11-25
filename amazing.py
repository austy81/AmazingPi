import RPi.GPIO as GPIO
import time

import player

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.ignorewarnin
buttonPin = 3
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

prev_state = True
while True:
    current_state = GPIO.input(buttonPin)
    if (current_state == False) and (prev_state == True):
        player.play()
    time.sleep(.1)
    prev_state = current_state