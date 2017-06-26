OpenCV - This repository hosts code for various python OpenCV projects that have been developed for the Raspberry Pi.

- Roadmap includes - 
  - Comparing two images (One face in source image) and looking for a similar face in the target (https://github.com/tangowhisky37/RaspiPythonProjects/tree/master/OpenCV/CaptureVideoStream) - 
    - Step 1 - Simple capture of images. (Done)
    - Step 2 -  Capture video and look for faces using OpenCV. (Done)
    - Step 3 -  Capture video, look for faces using OpenCV and once faces are found log image to disk. (Done)
    - Step 4 -  Capture video, look for faces using OpenCV and once faces are found log image to AWS S3. (Done)
    - Step 5 -  Capture video, look for faces using OpenCV, once faces are found log image to AWS S3, compare uploaded image to orignal image at S3 using AWS rekognition, display results of face comparison. (Done)
    - Step 6 -  Capture video, look for faces using OpenCV, once faces are found log image to AWS S3, compare uploaded image to orignal image at S3 using AWS rekognition, display results of face comparison, verbalise results using STT (Speech To Text). (Done)
    - Step 7 -  Capture video, look for faces using OpenCV, once faces are found log image to AWS S3, compare uploaded image to orignal image at S3 using AWS rekognition, display results of face comparison, verbalise results using STT (Speech To Text), call out local time, temperature and forecast for the day. (Done)
    - Step 8 -  Capture video, look for faces using OpenCV, once faces are found log image to AWS S3, compare uploaded image to orignal image at S3 using AWS rekognition, display results of face comparison, verbalise results using STT (Speech To Text), call out local time, temperature and forecast for the day, check time of last correct match and if < 60s ago do not perform STT functions. (Done)
    
  - Comparing two images (Many faces in source image) and looking for one of the known faces in the target -
    - Capture video, look for faces using OpenCV, once faces are found log image to AWS S3, compare uploaded image to orignal image (which now contains multiple faces in it) at S3 using AWS rekognition, display results of face comparison identifying which of the people in the original image have been identified, verbalise results using STT (Speech To Text), call out local time, temperature and forecast for the day, check time of last correct match and if < 60s ago do not perform STT functions. (In Progress)
    
  - Comparing two images (One face in source image) and looking for a similar face in the target. Implement AWS Lambda - 
    - Step 1 - Capture video, look for faces using OpenCV and once faces are found log image to AWS S3 all performed using one thread. Use AWS Lambda to launch a step function which compares uploaded image to orignal image at S3 using AWS rekognition and then uses SNS to send notification. Pick up notification on a separate thread, verbalise results using STT (Speech To Text), call out local time, temperature and forecast for the day, check time of last correct match and if < 60s ago do not perform STT functions. (Planned)

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
  - OpenCV Capture Images from VideoStream, Store on AWS S3, perform comparison of faces, call out to the identified person using STT (Speech To Text)
    - This project is designed to capture video from the Raspberry Pi camera and continuously scan the content for faces
    - This project using the Face Cascase HAAR filters and draws rectangles around the faces. 
    - Once faces have been identified in an image the image is logged to AWS S3
    - The code then calls the AWS Rekognition API to compare faces. If a positive match occurs it performs (Speech To Text) STT functions e.g. says hi, calls out the current weather, etc. 
    - Review code for the project at https://github.com/tangowhisky37/RaspiPythonProjects/tree/master/OpenCV/CaptureVideoStream 
  - The roadmap for this is always evolving. So check out the roadmap above to work out what's being currently worked upon. 
