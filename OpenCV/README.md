OpenCV - This repository hosts code for various python OpenCV projects that have been developed for the Raspberry Pi.

- Roadmap includes - 
  - Simple capture of images.
  - Capture video and look for faces.
  - Capture video, look for faces and once faces are found log image to disk.
  - Capture video, look for faces and once faces are found log image to AWS S3.
  - Capture video, look for faces, once faces are found log image to AWS S3 and send to AWS rekognition for comparison.
  - Capture video, look for faces, once faces are found log image to AWS S3, send to AWS rekognition for comparison and call out object found.

- Projects include - 
  - OpenCV Simple CaptureImage -
    - This was the first program i got started with. It's a very basic OpenCV program which warms up the camera and captures an image.
    - Review the code at - https://github.com/tangowhisky37/RaspiPythonProjects/tree/master/OpenCV/CaptureSingleImage
  - OpenCV Scan & CaptureFaces - 
    - FaceDetect1 - 
      - This piece of code was adopted from https://realpython.com/blog/python/face-recognition-with-python/. 
      - This code provides basic functionality to track faces. You can access the code at https://github.com/tangowhisky37/RaspiPythonProjects/tree/master/OpenCV/CaptureFaces/FaceDetect1
    - FaceDetect2 - 
      - This piece of code provides functionality to scan an image provided at the command line or as acquired from the Pi Camera with the objective of identifying faces. 
      - This project using the Face Cascase HAAR filters and draws rectangles around the faces on the captured image. 
      - Review the code at https://github.com/tangowhisky37/RaspiPythonProjects/tree/master/OpenCV/CaptureFaces/FaceDetect2
  - OpenCV Capture Images from VideoStream and store on AWS S3
    - This project is designed to capture video from the Raspberry Pi camera and continuously scan the content for faces
    - This project using the Face Cascase HAAR filters and draws rectangles around the faces. 
    - Once faces have been identified in an image the image is logged to AWS S3
    - Review code for the project at https://github.com/tangowhisky37/RaspiPythonProjects/tree/master/OpenCV/CaptureVideoStream
  - xxx
