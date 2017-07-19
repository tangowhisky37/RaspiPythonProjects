#!/bin/bash

i=0
while [ $i -eq 0 ]
do 
 sudo /usr/bin/fswebcam /var/www/html/usbcam/capturedimage.jpg
 sleep 2s
done
