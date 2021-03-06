#!/usr/bin/python

# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *
import os
import subprocess


proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidity.csv | cut -d , -f 2 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
roomtemp = out.strip()

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidity.csv | cut -d , -f 4 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
roomhumidity = out.strip()

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidityOWM.csv | cut -d , -f 2 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
outsidetemp = out.strip()

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidityOWM.csv | cut -d , -f 4 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
outsidehumidity = out.strip()


mylcd = RPi_I2C_driver.lcd()
mylcd.lcd_display_string("Room Temp - %s DegC" %roomtemp, 1)
mylcd.lcd_display_string("Room Hum - %s Pcnt" %roomhumidity, 2)
mylcd.lcd_display_string("Out Temp - %s DegC" %outsidetemp, 3)
mylcd.lcd_display_string("Out Hum - %s Pcnt" %outsidehumidity, 4)

sleep(5) # 5 sec delay

mylcd.lcd_clear()
mylcd.backlight(0)

