'''blinking led '''

import time
import RPi.GPIO as GPIO        #Import GPIO library
GPIO.setmode(GPIO.BOARD)       #use board pin numbering
GPIO.setup(7, GPIO.OUT)        #Setup GPIO pin 7 to out
while True:
       GPIO.output(7,True)     #Turn on led
       time.sleep(1)           #wait for one second
       GPIO.output(7,False)    #Turn off led
       time.sleep(1)           #wait for one second


 ''' Traffic light''' 
 import RPi.GPIO as GPIO
 from gpiozero import Button,TrafficLights
 from time import sleep

 button = Button(21)
 lights = TrafficLights(6, 22, 8)

 while True:
            button.wait_for_press()
            light.green.on()
            sleep(1)
            lights.off()
            lights.red.on()
            sleep(1)
            lights.off()
                
