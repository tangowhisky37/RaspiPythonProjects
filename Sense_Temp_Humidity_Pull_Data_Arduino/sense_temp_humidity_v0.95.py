#!/usr/bin/python

# Trevor W - The code to measure Humidity/Temp has been obtained from the Adafruit examples
# To execute the script - bash# sudo ./sense_temp_humidity_v0.7.py 11 4
# First input variable is the DHT11 or DHT22. Second input variable is the GPIO pin. Please use GPIO4.

# Including original copyright since part of the code (for the temp/humidity module) was obtained from Adafruit
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from gpiozero import LED
from gpiozero import Button
from signal import pause
from subprocess import *
import sys
import os
import time
import Adafruit_DHT
from time import sleep
import csv
import httplib, urllib
from lxml import html
import requests


redled = LED(17)
amberled = LED(22)
greenled = LED(27)
button = Button(2)

def WriteDataCSV():
 #Acquire data from Arduino, first for temp and next for humidity
 page = requests.get('http://10.100.10.10')
 tree = html.fromstring(page.content)
 bulletpoints = tree.xpath('//li/text()')
 #print bulletpoints[0]
 #print bulletpoints[1]
 #print bulletpoints[2]
 #print bulletpoints[3]
  
 #Obtaining temp
 string1 = bulletpoints[2]
 tempstringarray = string1.split(' ')
 temperature = tempstringarray[4]

 #Obtaining humidity
 string2 = bulletpoints[3]
 tempstringarray = string2.split(' ')
 humidity = tempstringarray[4]

 now = time.strftime("%d-%m-%Y %H:%M:%S")
 unit1 = "DegC"
 unit2 = "Percent"
 #outputFile = open('/opt/data/temphumidity.csv', 'wb')
 outputFile = open('/opt/data/temphumidity.csv', 'a')
 outputWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
 tempArray = [now,temperature,unit1,humidity,unit2]
 outputWriter.writerow(tempArray)
 outputFile.close()
 time.sleep(2)
 return


def WriteDataThingSpeak():
 #Acquire data from Arduino, first for temp and next for humidity
 page = requests.get('http://10.100.10.10')
 tree = html.fromstring(page.content)
 bulletpoints = tree.xpath('//li/text()')
 #print bulletpoints[0]
 #print bulletpoints[1]
 #print bulletpoints[2]
 #print bulletpoints[3]

 #Obtaining temp
 string1 = bulletpoints[2]
 tempstringarray = string1.split(' ')
 temperature = tempstringarray[4]

 #Obtaining humidity
 string2 = bulletpoints[3]
 tempstringarray = string2.split(' ')
 humidity = tempstringarray[4]

 #now = time.strftime("%d/%m/%Y %H:%M:%S")
 now = time.strftime("%d-%m-%Y %H:%M:%S")
 unit1 = "DegC"
 unit2 = "Percent"
 params = urllib.urlencode({'field1': temperature, 'field2': humidity, 'key':'2T23Y2A931XTAWCP'}) #Enter Key Here    
 headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
 conn = httplib.HTTPConnection("api.thingspeak.com:80")                
 try:
  conn.request("POST", "/update", params, headers)
  response = conn.getresponse()
  #Un-comment the below lines to see what's being logged & debug any issues with the code
  #print ("Data written to ThingSpeak : Temperature = {0:0.1f} DegC, Humidity = {1:0.1f}%".format(temperature,humidity))
  #print response.status, response.reason
  data = response.read()
  conn.close()
 except:
  print "Connection to ThingSpeak failed. Will try again next time."
 time.sleep(2)
 return

#Executing all modules only once since we are now executing from Cron
WriteDataCSV()
WriteDataThingSpeak()

