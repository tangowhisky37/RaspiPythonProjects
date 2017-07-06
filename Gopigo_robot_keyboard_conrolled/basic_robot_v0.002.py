#!/usr/bin/env python

from gopigo import *	#Has the basic functions for controlling the GoPiGo Robot
from subprocess import *
import sys	#Used for closing the running program

print "This is a basic example for the GoPiGo Robot control"
print "Press:\n\tp: Move GoPiGo Robot forward\n\tq: Turn GoPiGo Robot left\n\ta: Turn GoPiGo Robot right\n\tl: Move GoPiGo Robot backward\n\tt: Increase speed\n\tg: Decrease speed\n\tx: Stop GoPiGo Robot\n\tz: Exit\n"
while True:
	print "Enter the Command:",
	a=raw_input()	# Fetch the input from the terminal
	if a=='p':
                subprocess.call("espeak -v english-us 'moving forward'", shell=True)  
                led_on(0)
                led_on(1)
		fwd()	# Move forward
	elif a=='q':
                subprocess.call("espeak -v english-us 'turning left'", shell=True)  
                led_on(0)
                led_on(1)
		left()	# Turn left
	elif a=='a':
                subprocess.call("espeak -v english-us 'turning right'", shell=True)  
                led_on(0)
                led_on(1)
		right()	# Turn Right
	elif a=='l':
                subprocess.call("espeak -v english-us 'moving back'", shell=True)  
                led_on(0)
                led_on(1)
		bwd()	# Move back
	elif a=='x':
		stop()	# Stop
                led_off(0)
                led_off(1)
                subprocess.call("espeak -v english-us 'stopping'", shell=True)  
	elif a=='t':
		increase_speed()	# Increase speed
	elif a=='g':
		decrease_speed()	# Decrease speed
	elif a=='z':
		print "Exiting"		# Exit
		sys.exit()
	else:
		print "Wrong Command, Please Enter Again"
	time.sleep(.1)
#        print us_dist(15),'cm'
