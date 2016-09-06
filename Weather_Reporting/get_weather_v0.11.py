#!/usr/bin/python

from gpiozero import LED
from gpiozero import Button
from signal import pause
import subprocess
import sys
import os
import time
import Adafruit_DHT
from time import sleep
import csv
import httplib, urllib
import pyowm
import commands

owm = pyowm.OWM('XXXX')  # You MUST provide a valid API key

# Will it be sunny tomorrow at this time in Milan (Italy) ?
#forecast = owm.daily_forecast("Milan,it")
#tomorrow = pyowm.timeutils.tomorrow()
#forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('Melbourne,au')
w = observation.get_weather()

# Weather details
Wind = w.get_wind()                          # {'speed': 4.6, 'deg': 330} 
#SWind = w.get_wind()['speed']               # 4
Humidity = w.get_humidity()                  # 87
Temperature = w.get_temperature('celsius')   # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
Clouds = w.get_clouds()
Rainfall = w.get_rain() 
Pressure = w.get_pressure()  

#Output for debugging purpose
#print ("****************************************************************************************************")
#print ("Current wind Speed and Direction right now in Melbourne is =  %s " %Wind)     
#print ("Current Temperature in Melbourne is = %s" %Temperature)
#print ("Current Humidity in Melbourne is = %s Percent" %Humidity)
#print ("Cloud ceiling across Melbourne is %s thousand feet" %Clouds)
#print ("Current Rainfall across Melbourne is %s " %Rainfall)
#print ("Barometric Pressure across Melbourne is %s " %Pressure)
#print ("****************************************************************************************************")

#Obtain current Wind Speed
cmd = "echo " + str(Wind) + "| cut -f 1 -d , | cut -f 2 -d : > /tmp/wind.txt"
os.system(cmd)
OnlyWind = open('/tmp/wind.txt', 'r').read()
OnlyWind = ''.join(OnlyWind.split())
print ('Current wind speed is %s knots' %OnlyWind)

#Obtain current Temperature
cmd = "echo " + str(Temperature) + "| cut -d : -f 4 | cut -d , -f 1 > /tmp/temp.txt"
os.system(cmd)
OnlyTemp = open('/tmp/temp.txt', 'r').read()
#OnlyTemp.strip()
OnlyTemp = ''.join(OnlyTemp.split())
print ('Current Temperature is %s DegC' %OnlyTemp)

#Obtain current Min Temp
MinTemp = w.get_temperature('celsius')['temp_min']
print ('Current minimum temperature is %s DegC ' %MinTemp)

#Obtain current Max Temp
MaxTemp = w.get_temperature('celsius')['temp_max']
print ('Current maximum temperature is %s DegC ' %MaxTemp)

#Obtain current Humidity
print ("Current humidity is = %s Percent" %Humidity)

#Obtain current Cloud Ceiling
print ("Current cloud ceiling is %s (x00) feet" %Clouds)

#Obtain current Rainfall

#Obtain current Barometric Pressure
cmd = "echo " + str(Pressure) + "| cut -d : -f 2 | cut -d , -f 1 > /tmp/pressure.txt"
os.system(cmd)
OnlyPressure = open('/tmp/pressure.txt', 'r').read()
#OnlyPressure.strip()
OnlyPressure = ''.join(OnlyPressure.split())
print ('The Barometric Pressure is %s hPa' %OnlyPressure)


