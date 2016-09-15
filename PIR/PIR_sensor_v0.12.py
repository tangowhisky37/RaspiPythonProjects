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
     print("                  ")
     print("!!!!! Intruder Alert !!!!")
     print("                  ")
     buzzer.on()
     #cmd = "aplay /usr/share/scratch/Media/Sounds/Electronic/Whoop.wav"
     cmd = "aplay /home/pi/Downloads/TW_Experiments/Python_Projects/RaspiPythonProjects/PIR/70936__guitarguy1985__police.wav"
     os.system(cmd)
     time.sleep(30)
     buzzer.off()
     time.sleep(5)
    else:
     print("                  ")
     print("All good, no movement detected.")
     print("                  ")

