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

def WriteDataCSV(OnlyWind,OnlyTemp,OnlyPressure,Humidity,Clouds):
 #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
 if Humidity is not None and OnlyTemp is not None:
  now = time.strftime("%d-%m-%Y %H:%M:%S")
  unit1 = "DegC"
  unit2 = "Percent"
  unit3 = "hPa"
  unit4 = "Knots"
  unit5 = "x00 Feet"
  outputFile = open('/opt/data/temphumidityOWM.csv', 'a')
  outputWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  tempArray = [now,OnlyTemp,unit1,Humidity,unit2,OnlyPressure,unit3,OnlyWind,unit4,Clouds,unit5]
  outputWriter.writerow(tempArray)
  outputFile.close()
  time.sleep(5)
 else:
  print('Failed to get a reading. Will try again!')
  time.sleep(5)
 return


def WriteDataThingSpeak(OnlyWind,OnlyTemp,OnlyPressure,Humidity,Clouds):
 now = time.strftime("%d/%m/%Y %H:%M:%S")

 #Un-comment the below lines to see what's being logged & debug any issues with the code
 print ("****************************************************************************************************")
 print ("Data written to ThingSpeak : Wind Speed = %s Knots, Temperature = %s DegC, Pressure = %s hPa, Humidity = %s Percent, Cloud Ceiling = %s (x00)feet" %(OnlyWind, OnlyTemp, OnlyPressure, Humidity, Clouds))
 print ("****************************************************************************************************")

 params = urllib.urlencode({'field3': OnlyWind, 'field4': OnlyTemp, 'field5': OnlyPressure, 'field6': Humidity, 'field7': Clouds, 'key':'XXXXXXXX'}) # You MUST provide a valid API key
 headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
 conn = httplib.HTTPConnection("api.thingspeak.com:80")

 try:
  conn.request("POST", "/update", params, headers)
  response = conn.getresponse()
  print response.status, response.reason
  data = response.read()
  conn.close()
 except:
  print "Connection to ThingSpeak failed. Will try again next time."
  time.sleep(5)

 return


def WeatherProcessing():
 owm = pyowm.OWM('XXXXXXXXXX')  # You MUST provide a valid API key

 # Search for current weather in Melbourne (Australia)
 observation = owm.weather_at_place('Melbourne,au')
 w = observation.get_weather()

 #Get Weather details
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
 #cmd = "echo " + str(Wind) + "| cut -f 1 -d , | cut -f 2 -d : > /tmp/wind.txt"
 #os.system(cmd)
 #OnlyWind = open('/tmp/wind.txt', 'r').read()
 #OnlyWind = ''.join(OnlyWind.split()) # Strips away leading and trailing white space including newline, etc.
 OnlyWind = w.get_wind()['speed']
 print ("****************************************************************************************************")
 print ('Current wind speed is %s knots' %OnlyWind)

 #Obtain current Temperature
 #cmd = "echo " + str(Temperature) + "| cut -d : -f 4 | cut -d , -f 1 > /tmp/temp.txt"
 #os.system(cmd)
 #OnlyTemp = open('/tmp/temp.txt', 'r').read()
 #OnlyTemp.strip()                       # Strips away leading and trailing white space
 #OnlyTemp = ''.join(OnlyTemp.split())    # Strips away leading and trailing white space including newline, etc.
 OnlyTemp = w.get_temperature('celsius')['temp']
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

 #Obtain current Barometric Pressure
 cmd = "echo " + str(Pressure) + "| cut -d : -f 2 | cut -d , -f 1 > /tmp/pressure.txt"
 os.system(cmd)
 OnlyPressure = open('/tmp/pressure.txt', 'r').read()
 #OnlyPressure.strip()
 OnlyPressure = ''.join(OnlyPressure.split())
 print ('The Barometric Pressure is %s hPa' %OnlyPressure)

 WriteDataCSV(OnlyWind,OnlyTemp,OnlyPressure,Humidity,Clouds)

 WriteDataThingSpeak(OnlyWind,OnlyTemp,OnlyPressure,Humidity,Clouds)
 print ("****************************************************************************************************")
 print ("   ")
 print ("   ")
 time.sleep(30)
 return

while True:
 WeatherProcessing()
 time.sleep(30)

Pause()
