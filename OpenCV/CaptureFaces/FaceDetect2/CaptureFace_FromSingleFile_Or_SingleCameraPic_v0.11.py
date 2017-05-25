#!/home/pi/.virtualenvs/cv2/bin/python


import sys
from time import sleep
import cv2
import picamera

def extract_features(image):
    face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
    #nose_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/Nariz.xml')
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # iterate over all identified faces and try to find eyes
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, minSize=(30, 30))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

        #noses = nose_cascade.detectMultiScale(roi_gray, minSize=(100, 30))
        #for (ex,ey,ew,eh) in noses:
        #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    print "Found {0} faces in the picture!!!".format(len(faces))
    cv2.imshow('Mapping Faces within the Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        image_file = sys.argv[1]
    else:
        sleep(2)
        image_file = 'snapshot.jpg'
        picamera.PiCamera().capture(image_file)

    image = cv2.imread(image_file)
    extract_features(image)
