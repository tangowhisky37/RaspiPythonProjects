#!/usr/bin/python

import gpiozero 
import signal
import subprocess
import sys
import os
import time
from time import sleep
import csv
import httplib, urllib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)

while True :
 sensorvalue = GPIO.input(20)
 if sensorvalue == 0:
  print("Hey, I can sense that the room is illuminated.")
 elif sensorvalue == 1:
  print("Hey, I sense darkness.")
 else:
  print("Something's wrong. Let's wait for the next reading.")
 time.sleep(10) 
