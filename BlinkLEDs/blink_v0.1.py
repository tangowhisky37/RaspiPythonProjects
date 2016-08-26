from gpiozero import LED
from time import sleep
import sys

led = LED(17)

while True:
  led.on()
  sleep(0.5)
  led.off()
  sleep(0.5)
