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

#AWS Rekognition variables & code
bucket_source_var = "tw37-opencv"
#key_source_var = "new_image_name.jpg"
key_target_var = "orignal_trevor_1706.jpg"
bucket_target_var = "tw37-original"

def compare_faces(bucket, key, bucket_target, key_target, threshold=80, region="us-west-2"):
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
	return response['SourceImageFace'], response['FaceMatches']

#OWM Weather Data Functions
def WeatherProcessing():
 owm = pyowm.OWM('2866c7dec86f0ad873d0f626dafcd20e')  # You MUST provide a valid API key

 # Search for current weather in Melbourne (Australia)
 observation = owm.weather_at_place('Melbourne,au')
 w = observation.get_weather()

 #Get Weather details
 Wind = w.get_wind()                          # {'speed': 4.6, 'deg': 330}
 #SWind = w.get_wind()['speed']               # 4
 Humidity = w.get_humidity()                  # 87
 Temperature = w.get_temperature('celsius')   # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
 Clouds = w.get_clouds()
 Rainfall = w.get_rain()
 Pressure = w.get_pressure()

 #Output for debugging purpose
 print ("                                                         ")
 print ("                                                         ")
 print ("****************************************************************************************************")
 print ("Current wind Speed and Direction right now in Melbourne is =  %s " %Wind)
 print ("Current Temperature in Melbourne is = %s" %Temperature)
 print ("Current Humidity in Melbourne is = %s Percent" %Humidity)
 print ("Cloud ceiling across Melbourne is %s thousand feet" %Clouds)
 print ("Current Rainfall across Melbourne is %s " %Rainfall)
 print ("Barometric Pressure across Melbourne is %s " %Pressure)
 print ("****************************************************************************************************")
 print ("                                                         ")
 print ("                                                         ")
 

face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
#nose_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/Nariz.xml')

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))
s3 = boto3.client('s3')
time.sleep(2)

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
  bucket_source_var = "tw37-opencv"
  #key_source_var = "new_image_name.jpg"
  key_target_var = "orignal_trevor_1706.jpg"
  bucket_target_var = "tw37-original"

  source_face, matches = compare_faces(bucket_source_var, imagename, bucket_target_var, key_target_var) 
  print "Source Face ({Confidence}%)".format(**source_face)
  #one match for each target face
  for match in matches:
   print "Target Face ({Confidence}%)".format(**match['Face'])
   print "  Similarity : {}%".format(match['Similarity'])
   if (match['Similarity'] > 80):
    print "Hi Trevor, Welcome back."
    subprocess.call("espeak \" Hi Trevor Welcome back \" ", shell=True)
    WeatherProcessing()

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

