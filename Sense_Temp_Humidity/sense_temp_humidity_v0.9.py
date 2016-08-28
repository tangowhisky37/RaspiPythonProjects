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

redled = LED(17)
amberled = LED(27)
greenled = LED(22)
button = Button(2)

def WriteDataCSV():
 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
 if humidity is not None and temperature is not None:
  now = time.strftime("%d/%m/%Y %H:%M:%S")
  unit1 = "DegC"
  unit2 = "Percent"
  #outputFile = open('/opt/data/temphumidity.csv', 'wb')
  outputFile = open('/opt/data/temphumidity.csv', 'a')
  outputWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  tempArray = [now,temperature,unit1,humidity,unit2]
  outputWriter.writerow(tempArray)
  outputFile.close()
  time.sleep(2)
 else:
  print('Failed to get a reading. Will try again!')
  time.sleep(2)
 return


def WriteDataThingSpeak():
 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
 if humidity is not None and temperature is not None:
  now = time.strftime("%d/%m/%Y %H:%M:%S")
  unit1 = "DegC"
  unit2 = "Percent"
  #Input your ThingSpeak API Key below
  params = urllib.urlencode({'field1': temperature, 'field2': humidity, 'key':'InsertYourAPIKeyHere'})     
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


def ReadValues():
 # Try to grab a sensor reading.  Use the read_retry method which will retry up
 # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

 # Un-comment the line below to convert the temperature to Fahrenheit.
 # temperature = temperature * 9/5.0 + 32

 # Note that sometimes you won't get a reading and
 # the results will be null (because Linux can't
 # guarantee the timing of calls to read the sensor).
 # If this happens try again!
 if humidity is not None and temperature is not None:
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  print('!!!! Temperature = {0:0.1f} DegC, Humidity = {1:0.1f}% !!!!'.format(temperature, humidity))
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  time.sleep(1)
 else:
  print('Failed to get a reading. Will try again!')
  time.sleep(1)
 return

def SeeAndListen():
 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
 if humidity is not None and temperature is not None:
  if temperature >= 0 and temperature <= 10: 
   greenled.on()
   sleep(0.5)
   greenled.off()
   sleep(0.5)
   greenled.on()
   sleep(0.5)
   greenled.off()
   sleep(0.5)
   greenled.on()
   sleep(0.5)
   greenled.off()
   cmd="espeak 'The current temperature is " + str(temperature) + "Degrees Celcius and the humidity is" + str(humidity) + "Percent'"
   #Uncomment the below line if you would like to hear your Raspberry Pi speak
   #os.system(cmd)
   time.sleep(2)
   return
  elif temperature > 10 and temperature <= 20:
   amberled.on()
   sleep(0.5)
   amberled.off()
   sleep(0.5)
   amberled.on()
   sleep(0.5)
   amberled.off()
   sleep(0.5)
   amberled.on()
   sleep(0.5)
   amberled.off()
   cmd="espeak 'The current temperature is " + str(temperature) + "Degrees Celcius and the humidity is" + str(humidity) + "Percent'"
   #Uncomment the below line if you would like to hear your Raspberry Pi speak
   #os.system(cmd)
   time.sleep(2)
   return
  elif temperature > 20:
   redled.on()
   sleep(0.5)
   redled.off()
   sleep(0.5)
   redled.on()
   sleep(0.5)
   redled.off()
   sleep(0.5)
   redled.on()
   sleep(0.5)
   redled.off()
   cmd="espeak 'The current temperature is " + str(temperature) + "Degrees Celcius and the humidity is" + str(humidity) + "Percent'"
   #Uncomment the below line if you would like to hear your Raspberry Pi speak
   #os.system(cmd)
   time.sleep(2)
   return
 else:
  print('Failed to get a reading. I will not blink this time around. Will try again soon!!!')
  time.sleep(5)
  return

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

while True:
 WriteDataCSV()
 ReadValues() 
 SeeAndListen()
 WriteDataThingSpeak()
 time.sleep(30)

pause()

