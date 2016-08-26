from gpiozero import LED
from gpiozero import Button
from time import sleep
import sys
from signal import pause

led1 = LED(17)
led2 = LED(27)
button = Button(2)

#while True:
#	button.wait_for_press()
#	print('You asked for it smarty')
#	led.toggle()

#while True:
# if button.is_pressed:
#  print('You've just pressed the button')
#  led1.on()
#  sleep(0.5)
#  led1.off()
#  sleep(0.5)
#  led2.on()
#  sleep(0.5)
#  led2.off()
#  sleep(0.5)


button.when_pressed = led1.blink
button.when_released = led1.off

pause()
