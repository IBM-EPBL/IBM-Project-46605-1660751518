'''.....Blinking LED....'''

import time
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(11, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
while True:
	GPIO.output(11,True)  ## Turn on Led
	time.sleep(1)         ## Wait for one second
	GPIO.output(11,False) ## Turn off Led
	time.sleep(1)         ## Wait for one second


'''....Traffic Light....'''

import RPi.GPIO as GPIO
from gpiozero import Button, TrafficLights
from time import sleep    
        
button = Button(21)    
lights = TrafficLights(25, 8, 7)    
    
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
           
