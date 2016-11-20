#!/usr/bin/python

from time import *
import os
import sys 
import subprocess
import twitter

api = twitter.Api(consumer_key='jZdfgsdfgsdhdfghdfghdfjgD45V', consumer_secret='WwsNfzxfgdfgde56tdsfgzdfgsdfgm9ZKPdapLn6Mo4', access_token_key='77896786877857861297-JDSsdfdfgsdfgdbghghjfghjVsls', access_token_secret='6svPCxsI7Xkxvbterg44534dfgsdagsdfghhTwGVOGzg9pTz') #These are dummy keys, please replace with your original keys

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

#print("The temp inside is %s DegC, the temp outside is %s DegC, the humidity inside is %s Percent, the humidity outside is %s Percent, the airspeed is %s Knots and cloud cover is at %s x1000 feet." %(roomtemp, outsidetemp, roomhumidity, outsidehumidity, outairspeed, outcloudcover))

message = "The temp inside is " + roomtemp + " DegC, the temp outside is " + outsidetemp + " DegC, the humidity inside is " + roomhumidity + " Percent, the humidity outside is " + outsidehumidity + " Percent, the airspeed is " + outairspeed + " Knots and cloud cover is at " + outcloudcover + " x1000 feet." 
print message

status = api.PostUpdate(message)

