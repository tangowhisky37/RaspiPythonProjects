#!/home/pi/.virtualenvs/cv2/bin/python

from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
from time import sleep
import time
import cv2
import numpy as np
import sys
import datetime
import boto3
import subprocess 
import os
import pyowm
import commands
import multiprocessing
import threading
import json
import shlex

#AWS Rekognition variables 
bucket_target_var = "tw37-opencv"
#bucket_source_var = "new_image_name.jpg"
key_source_var = "orignal_trevor_1706.jpg"
bucket_source_var = "tw37-original"

#AWS Rekognition Code - Face Comparison 
def compare_faces(bucket, key, bucket_target, key_target, threshold=80, region="us-west-2"):
               
        #OWM Weather Data Functions
        owm = pyowm.OWM('xxxxxxx')  # You MUST provide a valid API key

        #Search for current weather in Melbourne (Australia)
        observation = owm.weather_at_place('Melbourne,au')
        w = observation.get_weather()

        #Get Weather details
        Wind = w.get_wind()                          # {'speed': 4.6, 'deg': 330}
        WindText = "espeak -g 10 \" Current wind Speed and Direction is " + format(Wind) + " \" "
        print (WindText)       

        SWind = w.get_wind()['speed']               # 4
        SWindText = "espeak -g 10 \" Current wind Speed is " + format(SWind) + " knots \" "

        Humidity = w.get_humidity()                  # 87
        HumidityText = "espeak -g 10 \" Current humidity is " + format(Humidity) + " percent \" "

        Temperature = w.get_temperature('celsius')   # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        TemperatureText = "espeak -g 10 \" Current temperature is " + format(Temperature) + " degrees \" "

        TemperatureAvg = w.get_temperature('celsius')['temp']   # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        TemperatureAvgText = "espeak -g 10 \" Current temperature is " + format(TemperatureAvg) + " degrees \" "

        Clouds = w.get_clouds()
        Rainfall = w.get_rain()
        Pressure = w.get_pressure()

        #Output for debugging purpose
        #print ("                                                         ")
        #print ("                                                         ")
        #print ("****************************************************************************************************")
        #print ("Current wind Speed and Direction right now in Melbourne is =  %s " %Wind)
        #print ("Current Temperature in Melbourne is = %s" %Temperature)
        #print ("Current Humidity in Melbourne is = %s Percent" %Humidity)
        #print ("Cloud ceiling across Melbourne is %s thousand feet" %Clouds)
        #print ("Current Rainfall across Melbourne is %s " %Rainfall)
        #print ("Barometric Pressure across Melbourne is %s " %Pressure)
	#print ("****************************************************************************************************")
        #print ("                                                         ")
        #print ("                                                         ") 

        #Face Matching Code Starts Here
	rekognition = boto3.client("rekognition", region)
	response = rekognition.compare_faces(
	    SourceImage={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		TargetImage={
			"S3Object": {
				"Bucket": bucket_target,
				"Name": key_target,
			}
		},
	    SimilarityThreshold=threshold,
	)

        #print(response)
        temp1 = json.dumps(response)
        temp2 = json.loads(temp1)
        #print(temp2['FaceMatches'])
        print "Source Face Confidence in %s " %format(temp2['SourceImageFace']['Confidence'])
        for match in temp2['FaceMatches']:
         print "Similarity between compared faces is %s " %format(temp2['FaceMatches'][0]['Similarity'])
         subprocess.call('espeak \" Hi Trevor Welcome back \" ', shell=True)
         #subprocess.call(shlex.split(WindText))
         subprocess.call(shlex.split(SWindText))
         subprocess.call(shlex.split(HumidityText))
         subprocess.call(shlex.split(TemperatureAvgText))
         #WeatherProcessing()
        for nomatch in temp2['UnmatchedFaces']:
         print "Faces either don't match or are a poor match"
	return

 
#Main Code Section Starts Here
face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
#nose_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/Nariz.xml')

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))
s3 = boto3.client('s3')
time.sleep(2)

#Clearing the buffer before loading the first image
rawCapture.truncate(0)

while True:
 #time.sleep(1)
 camera.capture(rawCapture, format="bgr")
 img = rawCapture.array
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 gray = cv2.GaussianBlur(gray, (21, 21), 0)
 faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

 # iterate over all identified faces and try to find eyes
 for (x, y, w, h) in faces:
   cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = img[y:y+h, x:x+w]

   #The code on the next three lines works and has been tested out
   #Disabling it because it's not required for purposes of identification of faces
   #eyes = eye_cascade.detectMultiScale(roi_gray, minSize=(30, 30))
   #for (ex,ey,ew,eh) in eyes:
     #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

     #Detection of code for noses has not been validated or tested
     #noses = nose_cascade.detectMultiScale(roi_gray, minSize=(100, 30))
     #for (ex,ey,ew,eh) in noses:
     #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

 #printing messages to the screen
 print "At time "+time.strftime("%d/%m/%y-%H:%M:%S")+", found {0} faces in the picture!!!".format(len(faces))

 #writing the image to the screen
 font = cv2.FONT_HERSHEY_SIMPLEX
 #cv2.putText(img, str(datetime.datetime.now().strftime("%d/%m/%y-%H/%M/%S")), (100,500), font, 4,(255,255,255),2) 
 cv2.putText(img, "DateTime - "+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")), (5,25), font, 0.5,(255,255,255)) 
 cv2.imshow('Mapping Faces within the Image', img)

 #writing the image to a file
 if len(faces) > 0:
  #Older versions of cv2.imwrite
  #cv2.imwrite("temp"+str(time.strftime("%d/%m/%y-%H%M%S"))+".jpg",img)
  #cv2.imwrite("temp"+str(datetime.datetime.now())+".jpg",img)
  #cv2.imwrite("temp"+str(datetime.datetime.now().strftime("%d/%m/%y-%H/%M/%S"))+".jpg",img)
  #cv2.imwrite("FaceCaptureWarrenPi-"+str(datetime.datetime.now())+".jpg",img)
  
  #current version of cv2.imwrite
  #imagename = "FaceCaptureWarrenPi-" + format(str(datetime.datetime.now())) + ".jpg" #This also works 
  imagename = "FaceCaptureWarrenPi-" + format(str(time.strftime("%d%m%y-%H%M%S"))) + ".jpg" 
  writepath = "/home/pi/Downloads/TW_Experiments/Python_Projects/RaspiPythonProjects/OpenCV/CaptureVideoStream/imagecapture/" + imagename
  cv2.imwrite(writepath, img)
  print "Captured image to file !!!"

  #Uploading files to AWS S3
  with open(writepath, 'rb') as data:
   s3.upload_fileobj(data, "tw37-opencv", imagename) 
 
  #Comparing images using AWS Rekognition
  bucket_target_var = "tw37-opencv"
  #key_target_var = "new_image_name.jpg"
  key_source_var = "orignal_trevor_1706.jpg"
  bucket_source_var = "tw37-original"

  #source_face, matches = compare_faces(bucket_source_var, key_source_var, bucket_target_var, imagename) 
  #print "Source Face ({Confidence}%)".format(**source_face)
  #one match for each target face
  #for match in matches:
  # print "Target Face ({Confidence}%)".format(**match['Face'])
  # print "  Similarity : {}%".format(match['Similarity'])
  # if (match['Similarity'] > 80):
  #  print "Hi Trevor, Welcome back."
  #  subprocess.call("espeak \" Hi Trevor Welcome back \" ", shell=True)
  #  WeatherProcessing()
 
  #Forking a thread to perform the AWS Rekognition Comparison
  threads = []
  t = threading.Thread(target=compare_faces, args=(bucket_source_var, key_source_var, bucket_target_var, imagename))
  threads.append(t)
  t.start()


 #looking for escape sequence
 key = cv2.waitKey(1) & 0xFF
 if key == ord("q"):
    print "Quitting....hold on"
    break
 
 #Clearing the buffer before loading the next image
 rawCapture.truncate(0)

#Closing the capture, releasing all resources
#rawCapture.release()
cv2.destroyAllWindows() 

