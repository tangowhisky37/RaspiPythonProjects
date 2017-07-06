#!/usr/bin/env python

from gopigo import *
import time
import sys


def lights_on():
  led_on(0) #Switching on LED 0
  led_on(1) #Switching on LED 1

def lights_off():
  led_off(0) #Switching off LED 0
  led_off(1) #Switching off LED 1

def reset_servo():
  enable_servo()
  servo(0)
  time.sleep(2)
  #servo(180)
  #time.sleep(2)
  servo(80)
  time.sleep(2)
  disable_servo()

def set_gpg_speed():
  set_left_speed(150)
  set_right_speed(150)

def move_forward():
  reset_servo()
  subprocess.call("espeak -v english-us 'moving forward'", shell=True)
  set_gpg_speed()
  fwd()	
  while True:
   dist=us_dist(15)
   if dist>distance_to_stop:
    print "Distance to object is ",dist, "cm" 
   else: 
    stop()
    subprocess.call("espeak -v english-us 'stopping'", shell=True)
    time.sleep(2)
    subprocess.call("espeak -v english-us 'reversing'", shell=True)
    set_gpg_speed()
    bwd()
    time.sleep(1)
    #lights_off()
    stop()
    time.sleep(2)
    distance_gauge()
    #break
    #time.sleep(.1)

def distance_gauge():
  subprocess.call("espeak -v english-us 'checking optimal route'", shell=True)
  enable_servo()
  lights_off()
  lights_on()
  servo(0)
  distance1=us_dist(15)
  lights_off()
  time.sleep(1)
  lights_on()
  servo(45)
  distance2=us_dist(15)
  lights_off()
  time.sleep(1)
  lights_on()
  servo(90)
  distance3=us_dist(15)
  lights_off()
  time.sleep(1)
  lights_on()
  servo(135)
  distance4=us_dist(15)
  lights_off()
  time.sleep(1)
  lights_on()
  servo(160)
  distance5=us_dist(15)
  lights_off()
  time.sleep(1)
  lights_on()
  reset_servo()
  #disable_servo()
  if distance1>distance5:
   subprocess.call("espeak -v english-us 'turning right mate'", shell=True)
   #right_rot()
   set_gpg_speed()
   right()
   time.sleep(.05)
   subprocess.call("espeak -v english-us 'stopping'", shell=True)
   stop()
   time.sleep(1)
   subprocess.call("espeak -v english-us 'moving forward mate'", shell=True)
   move_forward()
  elif distance5>distance1:
   subprocess.call("espeak -v english-us 'turning left mate'", shell=True)
   #left_rot()
   left()
   set_gpg_speed()
   time.sleep(.05)
   subprocess.call("espeak -v english-us 'stopping'", shell=True)
   stop()
   time.sleep(1)
   subprocess.call("espeak -v english-us 'moving forward mate'", shell=True)
   move_forward()
  else: 
   subprocess.call("espeak -v english-us 'Am blocked on all sides darling. Get me out of here.'", shell=True)
   stop 
   lights_off()


distance_to_stop=70
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print "!!!! Press ENTER to get going !!!!"
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
raw_input()
lights_on()
move_forward()


