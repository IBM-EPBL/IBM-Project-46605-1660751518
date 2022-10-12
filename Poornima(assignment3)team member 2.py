'''Blinking LED'''

import time
import Rpi.GPIO as GPIO    ##Import GPIO library
GPIO.setmode(GPIO.BOARD)   ##Use board pin numbering
GPIO.setup(13,GPIO.OUT)    ##Setup GPIO pin 19 to OUT
while True:
    GPIO.output(13,True)   ##Turn on LED
    time.sleep(1)          ##Wait for one second
    GPIO.output(13,False)  ##Turn off LED
    time.sleep(1)          ##Wait for one second
    


'''Traffic Light'''

import RPi.GPIO as GPIO
from gpiozero import Button,TrafficLights
from time import sleep

button=Button(21)
lights=TrafficLights(25,8,7)
while True:
    button.wait_for_press()
    light.green.on()
    sleep(1)
    lights.off()
    lights.amber.on()
    sleep(1)
    lights.off()
    lights.red.on()
    sleep(1)
    lights.off()
