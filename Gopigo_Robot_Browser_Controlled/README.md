## Stream Video & Control Your Robot via Your Web Browser 
### This project is aimed at building a Robot that allows for streaming of video and control from a web browser

* Here are some pictures of what you will end up with. This project has been built upon the Dexter Industries GoPiGo robot.
* Dexter Industries offers a modular robot with excellent video, printed tutorials to getting you up and running in a few hours. 
* The initial Dexter Industries robots were based on the Rapsberry Pi 2 (which is what my robot is based upon) but have now upgraded their robot package to support the Raspberry Pi 3.
* You can read more about this robot and pick your up from [Dexter Industries](http://www.dexterindustries.com)
* A lot of the code and functions included here are leveraged from Dexter Industries examples which are licensed under GPL.

![Mobile control of the GoPiGo Raspberry Pi Robot](https://raw.githubusercontent.com/DexterInd/GoPiGo/master/Software/Python/Examples/Browser_Streaming_Robot/Raspberry_Pi_Camera_controlled-by-mobile-browser.jpg "Control of the GoPiGo Raspberry Pi Robot with a mobile phone.")

![Robot Control and streaming through the browser](https://raw.githubusercontent.com/DexterInd/GoPiGo/master/Software/Python/Examples/Browser_Streaming_Robot/Raspberry_Pi_Camera_streaming-to-computer-browser.jpg "Streaming video through the browser of the GoPiGo")

![Controlling the GoPiGo robot with a mobile phone](https://raw.githubusercontent.com/DexterInd/GoPiGo/master/Software/Python/Examples/Browser_Streaming_Robot/Raspberry_Pi_Camera_controlled-by-mobile-browser.jpg "Streaming video from your Raspberry Pi Robot to your mobile phone.")

**Usage:**
- Make robot_web_server.py executable

 >      bash# chmod +x robot_web_server.py

- Run robot_web_server.py which launches the Python Tornado web server
- Open a web browser on any computer or mobile device and enter the following in the address bar:

 >      http://IP_Address_Of_Your_Raspberry_Pi:98

- The page that hosts the streaming video and browser control application runs on the local IP address of the Pi on port 98
- The video stream would load up and you can use the joystick on the screen to control the GoPiGo

![ GoPiGo ](https://raw.githubusercontent.com/DexterInd/GoPiGo/master/GoPiGo_Chassis-300.jpg)

![ GoPiGo ](https://raw.githubusercontent.com/DexterInd/GoPiGo/master/GoPiGo_Front_Facing_Camera300.jpg)

Enjoy and keep hacking !!!
