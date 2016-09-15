#!/usr/bin/python

from gpiozero import MotionSensor, Buzzer
import signal
import subprocess
import sys
import os
import time
from time import sleep

pir = MotionSensor(20)
buzzer = Buzzer(19)

while True:
    if pir.motion_detected:
     print("You moved")
     buzzer.on()
     time.sleep(1)
     buzzer.off()
     time.sleep(5)
    else:
     print("No movement detected")

