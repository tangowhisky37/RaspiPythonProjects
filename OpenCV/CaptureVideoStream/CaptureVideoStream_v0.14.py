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


face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
#nose_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/Nariz.xml')

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))
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
  #cv2.imwrite("temp"+str(time.strftime("%d/%m/%y-%H%M%S"))+".jpg",img)
  #cv2.imwrite("temp"+str(datetime.datetime.now())+".jpg",img)
  #cv2.imwrite("temp"+str(datetime.datetime.now().strftime("%d/%m/%y-%H/%M/%S"))+".jpg",img)
  cv2.imwrite("FaceCaptureWarrenPi-"+str(datetime.datetime.now())+".jpg",img)
  print "Captured image to file !!!"

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

