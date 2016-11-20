#!/usr/bin/python

from time import *
import os
import subprocess

#cmd = "sudo rmmod i2c_bcm2708; sudo modprobe i2c_bcm2708;"
#os.system(cmd)

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidity.csv | cut -d , -f 2 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
roomtemp = out.strip()

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidity.csv | cut -d , -f 4 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
roomhumidity = out.strip()

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidityOWM.csv | cut -d , -f 2 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
outsidetemp = out.strip()

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidityOWM.csv | cut -d , -f 4 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
outsidehumidity = out.strip()

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidityOWM.csv | cut -d , -f 8 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
outairspeed = out.strip()

proc = subprocess.Popen(["tail -n 1 /opt/data/temphumidityOWM.csv | cut -d , -f 10 | cut -d \\\" " + "-f 2"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
outcloudcover = out.strip()

#cmd = "sudo rmmod i2c_bcm2708; sudo modprobe i2c_bcm2708;"
#os.system(cmd)
print("The temp inside is %s DegC, the temp outside is %s DegC, the humidity inside is %s Percent, the humidity outside is %s Percent, the airspeed is %s Knots and cloud cover is at %s x1000 feet." %(roomtemp, outsidetemp, roomhumidity, outsidehumidity, outairspeed, outcloudcover))

