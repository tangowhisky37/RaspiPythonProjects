#!/usr/bin/python

# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *
import os
import subprocess

#Raspberry Pi 3 doesn't detect the connected I2C devices
#The code below (removal and insertion of I2C modules) is required to 
#force detection of attached devices
#cmd = "sudo rmmod i2c_bcm2708; sudo modprobe i2c_bcm2708;"
#os.system(cmd)

while True:
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

 proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidityOWM.csv | cut -d , -f 8 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
 (out, err) = proc.communicate()
 #print "program output:", out
 outairspeed = out.strip()

 proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidityOWM.csv | cut -d , -f 10 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
 (out, err) = proc.communicate()
 #print "program output:", out
 outcloudcover = out.strip()

 #Raspberry Pi 3 doesn't detect the connected I2C devices
 #The code below (removal and insertion of I2C modules) is required to
 #force detection of attached devices
 cmd = "sudo rmmod i2c_bcm2708; sudo modprobe i2c_bcm2708;"
 os.system(cmd)
 mylcd = RPi_I2C_driver.lcd()
 mylcd.lcd_display_string("RoomTemp %s DegC" %roomtemp, 1)
 mylcd.lcd_display_string("OutTemp %s DegC" %outsidetemp, 2)
 #mylcd.lcd_display_string_pos("OtTp %s C" %outsidetemp,1,11)  //Tried displaying both in one line but doesn't quite work
 mylcd.lcd_display_string("RmHumidity %s Pcnt" %roomhumidity, 3)
 mylcd.lcd_display_string("OutHumidity %s Pcnt" %outsidehumidity, 4)
 #disabling sleep, lcd_clear() and lcd_backlight() to let the information remain on the screen
 #sleep(5) # 5 sec delay
 #mylcd.lcd_clear()
 #mylcd.backlight(0)
 sleep(300) # delay

 cmd = "sudo rmmod i2c_bcm2708; sudo modprobe i2c_bcm2708;"
 os.system(cmd)
 mylcd = RPi_I2C_driver.lcd()
 mylcd.lcd_clear()
 mylcd.lcd_display_string("RoomTemp %s C" %roomtemp, 1)
 mylcd.lcd_display_string("OutTemp %s C" %outsidetemp, 2)
 mylcd.lcd_display_string("Airspeed %s Knots" %outairspeed, 3)
 mylcd.lcd_display_string("Clouds %s00 Feet" %outcloudcover, 4)
 #disabling sleep, lcd_clear() and lcd_backlight() to let the information remain on the screen
 #sleep(5) # 5 sec delay
 #mylcd.lcd_clear()
 #mylcd.backlight(0)
 sleep(300) # delay
 
 #mylcd.lcd_display_string(" !!! Downloading Updates !!!", 2)
 #sleep(5) # 5 sec delay
 #mylcd.lcd_clear()
 #mylcd.backlight(0)

