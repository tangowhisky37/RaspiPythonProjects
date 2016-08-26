from gpiozero import LED
from gpiozero import Button
from time import sleep
import sys
from signal import pause
from subprocess import *
import os

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
button = Button(2)

#while True:
#	button.wait_for_press()
#	print('You asked for it smarty')
#	led.toggle()

while True:
 if button.is_pressed:
  print('Here goes the Red LED')
  os.system("espeak red")
  led1.on()
  sleep(0.5)
  led1.off()
  sleep(0.5)
  print('Here goes the Amber LED')
  os.system("espeak amber")
  led2.on()
  sleep(0.5)
  led2.off()
  sleep(0.5)
  print('Here goes the Green LED')
  os.system("espeak green")
  led3.on()
  sleep(0.5)
  led3.off()
  sleep(0.5)


#button.when_pressed = led.blink
#button.when_released = led.off

pause()
