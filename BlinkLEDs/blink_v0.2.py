from gpiozero import LED
from gpiozero import Button
from time import sleep
import sys

led = LED(17)
button = Button(2)

button.wait_for_press()
print('You asked for it smarty')
#led.on()
#sleep(5)
#led.off()

while True:
  led.on()
  sleep(0.5)
  led.off()
  sleep(0.5)
