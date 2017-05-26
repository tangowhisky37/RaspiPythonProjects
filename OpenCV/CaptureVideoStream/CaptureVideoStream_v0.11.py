#!/home/pi/.virtualenvs/cv2/bin/python

from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import time
import cv2
import numpy as np
import sys
from time import sleep


face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
#nose_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/Nariz.xml')

capture = cv2.VideoCapture(0)

while True:
 ret, img = capture.read()
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

 # iterate over all identified faces and try to find eyes
 for (x, y, w, h) in faces:
   cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = img[y:y+h, x:x+w]

   eyes = eye_cascade.detectMultiScale(roi_gray, minSize=(30, 30))
   for (ex,ey,ew,eh) in eyes:
     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

     #noses = nose_cascade.detectMultiScale(roi_gray, minSize=(100, 30))
     #for (ex,ey,ew,eh) in noses:
     #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

 print "Found {0} faces in the picture!!!".format(len(faces))
 cv2.imshow('Mapping Faces within the Image', img)
 #cv2.waitKey(0)
 #cv2.destroyAllWindows()
 key = cv2.waitKey(1) & 0xFF
 if key == ord("q"):
    break
capture.release()
cv2.destroyAllWindows() 


