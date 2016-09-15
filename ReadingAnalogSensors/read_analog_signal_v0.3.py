#!/usr/bin/python

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
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


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
#SPI_PORT   = 0
#SPI_DEVICE = 0
#mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


def WriteDataCSV(LDRSensorValue):
 if LDRSensorValue is not None:
  now = time.strftime("%d-%m-%Y %H:%M:%S")
  unit1 = "Value"
  outputFile = open('/opt/data/AnalogSensorData.csv', 'a')
  outputWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  tempArray = [now,LDRSensorValue,unit1]
  outputWriter.writerow(tempArray)
  outputFile.close()
  time.sleep(5)
 else:
  print('Failed to get a reading. Will try again!')
  time.sleep(5)
 return


def WriteDataThingSpeak(LDRSensorValue):
 now = time.strftime("%d/%m/%Y %H:%M:%S")

 #Un-comment the below lines to see what's being logged & debug any issues with the code
 print "*******************************************************************"
 print ("Data written to ThingSpeak : LDR Sensor Value is %s" %(LDRSensorValue))
 print "*******************************************************************"

 params = urllib.urlencode({'field8': LDRSensorValue, 'key':'XXXX'}) # You MUST provide a valid API key
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


def AnalogDataProcessing():

 #Obtaining Analog measurement for MCP 3008 Pin 0
 LDRSensorValue = mcp.read_adc(0)
 print "      "
 print ("The Protosensitive LDR Sensor reading is %s " %LDRSensorValue)
 print "      "

 WriteDataCSV(LDRSensorValue)
 WriteDataThingSpeak(LDRSensorValue)
 print ("   ")
 time.sleep(5)
 return

#Calling Main function once
AnalogDataProcessing()


