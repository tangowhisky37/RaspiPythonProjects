#!/bin/bash

sudo /sbin/rmmod i2c_bcm2708
sudo /sbin/modprobe i2c_bcm2708
cd /home/pi/Downloads/TW_Experiments/Python_Projects/RaspiPythonProjects/LCD_Write/
./WriteToScreenv0_13.py
