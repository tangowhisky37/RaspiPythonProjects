#!/usr/bin/python

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
 page = requests.get('http://192.168.1.24')
 tree = html.fromstring(page.content)
 bulletpoints = tree.xpath('//ul/text()')
 #print bulletpoints[0]
 #print bulletpoints[1]
 #print bulletpoints[2]
 #print bulletpoints[3]
  
 #Obtaining temp
 string1 = bulletpoints[0]
 tempstringarray = string1.split(' ')
 temperature = tempstringarray[4].strip()
 print "temperature - " + temperature

 #Obtaining humidity
 string2 = bulletpoints[2]
 tempstringarray = string2.split(' ')
 humidity = tempstringarray[2].strip()
 print "humidity - " + humidity

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
 page = requests.get('http://192.168.1.24')
 tree = html.fromstring(page.content)
 bulletpoints = tree.xpath('//ul/text()')
 #print bulletpoints[0]
 #print bulletpoints[1]
 #print bulletpoints[2]
 #print bulletpoints[3]

 #Obtaining temp
 string1 = bulletpoints[0]
 tempstringarray = string1.split(' ')
 temperature = tempstringarray[4].strip()
 print "temperature - " + temperature

 #Obtaining humidity
 string2 = bulletpoints[2]
 tempstringarray = string2.split(' ')
 humidity = tempstringarray[2].strip()
 print "humidity - " + humidity

 #now = time.strftime("%d/%m/%Y %H:%M:%S")
 now = time.strftime("%d-%m-%Y %H:%M:%S")
 unit1 = "DegC"
 unit2 = "Percent"
 params = urllib.urlencode({'field1': temperature, 'field2': humidity, 'key':'xxxxxxx'}) #Enter Key Here    
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

