#!/usr/bin/python

# Trevor W - The code to measure Humidity/Temp has been obtained from the Adafruit examples
#
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

redled = LED(17)
amberled = LED(27)
greenled = LED(22)
button = Button(2)

def WriteData():
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
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  print('The current Temperature is {0:0.1f} Degrees Celcius while the current Humidity is {1:0.1f}%'.format(temperature, humidity))
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  time.sleep(1)
 else:
  print('Failed to get a reading. Will try again!')
  time.sleep(1)
 return

def SeeAndListen():
 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
 if humidity is not None and temperature is not None:
  #print('The current Temperature is {0:0.1f} Degrees Celcius while the current Humidity is {1:0.1f}%'.format(temperature, humidity))
  if temperature >= 0 and temperature <= 10: 
   greenled.on()
   sleep(0.5)
   greenled.off()
   sleep(0.5)
   greenled.on()
   sleep(0.5)
   greenled.off()
   cmd="espeak 'The current temperature is " + str(temperature) + "Degrees Celcius and the humidity is" + str(humidity) + "Percent'"
   os.system(cmd)
   time.sleep(60)
   return
  elif temperature > 10 and temperature <= 20:
   amberled.on()
   sleep(0.5)
   amberled.off()
   sleep(0.5)
   amberled.on()
   sleep(0.5)
   amberled.off()
   cmd="espeak 'The current temperature is " + str(temperature) + "Degrees Celcius and the humidity is" + str(humidity) + "Percent'"
   os.system(cmd)
   time.sleep(60)
   return
  elif temperature > 20:
   redled.on()
   sleep(0.5)
   redled.off()
   sleep(0.5)
   redled.on()
   sleep(0.5)
   redled.off()
   cmd="espeak 'The current temperature is " + str(temperature) + "Degrees Celcius and the humidity is" + str(humidity) + "Percent'"
   os.system(cmd)
   time.sleep(60)
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
 ReadValues() 
 SeeAndListen()
 WriteData()

pause()

