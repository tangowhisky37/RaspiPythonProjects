#!/usr/bin/env python

from gopigo import *
import time
import sys

led_on(0) #Switching on LED 0
led_on(1) #Switching on LED 1
 
distance_to_stop=40		
print "!!!! Press ENTER to get going !!!!"
raw_input()		

def move_forward():
  subprocess.call("espeak -v english-us 'moving forward'", shell=True)
  fwd()	
  while True:
   dist=us_dist(15)
   if dist>distance_to_stop:
    print "Distance to object is ",dist, "cm" 
   else: 
    subprocess.call("espeak -v english-us 'stopping'", shell=True)
    led_off(0) #Switching off LED 0
    led_off(1) #Switching off LED 1
    stop()
    break
    time.sleep(.1)

move_forward()
