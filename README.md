# RaspiPythonProjects

This folder contains a list of all the Raspberry Pi projects I have been working on


BlinkLEDs
- This folder includes programs that uses the Raspberry Pi's GPIO pins to interact with multiple LED's
- This folder also includes programs that use the Raspberry Pi's GPIO pins to interact with a simple push button
- Components required for the programs in this folder include 
  - 1 x Raspberry Pi 3 (I have used a 3, Model B. You can use whatever you have at your disposal.)
  - 3 x 50 Ohm Resistors
  - 3 x LED's
  - LED's connected to the following GPIO ports : led1 on GPIO17, led2 on GPIO27, led3 on GPIO22
  - 1 x Breadboard
  - 1 x Extension cable (Suggested) to extend the GPIO ports of the Raspberry Pi and bring them closed to the breadboard 
  - 6 x Jumper cables - Female (connect to Rasberry Pi GPIO) to Male (Connect to the Breadboard)
  - 1 x Tactile Push button
  - 1 x Raspberry Pi Cobbler board (Recommended, to breakout the GPIO's) and make working easier
- For circuit and connectivity details please refer to the images in the respective directories
- For additional reading please visit 
  - https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/


IoT - Sense_Temp_Humidity (Log to CSV and ThingSpeak/IoT Platform)
- Components required for the programs in this folder include
  - 1 x Raspberry Pi 3 (I have used a 3, Model B. You can use whatever you have at your disposal.)
  - 3 x 50 Ohm Resistors
  - 1 x 10 KOhm Resistors
  - 3 x LED's
  - LED's connected to the following GPIO ports : Red LED on GPIO17, amber LED on GPIO27, Green LED on GPIO22
  - 1 x Breadboard
  - 1 x Extension cable (Suggested) to extend the GPIO ports of the Raspberry Pi and bring them closed to the breadboard
  - 6 x Jumper cables - Female (connect to Rasberry Pi GPIO) to Male (Connect to the Breadboard)
  - 4 x Jumper cables - Female (connect to Rasberry Pi GPIO) to Male (Connect to the Breadboard)
  - 1 x Tactile Push button
  - 1 x Raspberry Pi Cobbler board (Recommended, to breakout the GPIO's) and make working easier
  - 1 x Arduino compatible Temperature and Humidity sensor 
    - http://www.jaycar.com.au/arduino-compatible-temperature-and-humidity-sensor-module/p/XC4520
    - https://littlebirdelectronics.com.au/products/arduino-compatible-temperature-and-humidity-sensor-module
    - https://tkkrlab.nl/wiki/Arduino_KY-001_Temperature_sensor_module
    - https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing
    - https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/
    - Sensor should be connected to GPIO04 (Pin 7) 
  - 1 x Speaker connected to the Raspberry Pi if you want it to speak
  - 1 x 3.5mm Audio cable to connect the speaker to the Raspberry Pi
- Python Adafruit DHT Library - https://github.com/adafruit/Adafruit_Python_DHT
- Data directory to log captured data in CSV form in /opt/data. 
  - The folder /opt/data will need to be created.
  - Permissions on the folder to be granted to user executing the program.
- To log data at the ThingSpeak IoT platform, create an account at ThingSpeak (https://thingspeak.com). 
  - This program uses the DHT11 and logs both Temperatury, Humidity
  - Create a new channel at Thingspeak. Create two new fields at ThingSpeak i.e. field1, field2
  - Copy your API key to the program and update the WriteDataThinkSpeak() function.
  - This program has now been updated to pull data from a local Arduino Mega 2560 over http. The Arduino has a DHT11 connected to it.
  - The Arduino also includes an Ethernet module based on the enc28j60 chip allowing it to connect over the network.
  - For details on connecting up the Arduino and configuring the ethernet module please refer to my contribution at ArduinoProjects here on Github.


Weather Reporting using OWM (Log to CSV and ThingSpeak/IoT Platform)
- While the Sense_Temp_Humidity project (above) was designed as a simple IoT (Internet Of Things) project to pull data from my DHT11 on the Raspberry Pi to be uploaded to ThingSpeak, Weather Reporting on the other hand pulls data from OpenWeatherMap and uploads the data to Thingspeak.
- The objective of this project was to be able to compare the data for temperature, humidity being collected by my sensors at home with the data for the city i live in provided by Open Weather Map.
- The project uses the Open Weather Map python library which you will need to download and install on the Raspberry Pi
- Components required include - 
 - Python module for OWM from https://github.com/csparpa/pyowm
 - 1 x Raspberry Pi 3 (I have used a 3, Model B. You can use whatever you have at your disposal.


Simple light sensor 
- The Simple Light Sensor is a very simple program that detects the presence of light or darkness
- Components required include -
  - 1 x Raspberry Pi 3 (I have used a 3, Model B. You can use whatever you have at your disposal.)
  - 1 x Photoresistor Light Sensor module
    - http://www.buildcircuit.com.au/Photoresistor-Sensor-Module-Light-Detection-for-arduino
    - http://www.dx.com/p/6495-photoresistor-light-sensor-module-for-smart-car-black-blue-152774
    - https://tkkrlab.nl/wiki/Arduino_KY-018_Photo_resistor_module 
    - The first two links very closely resemble the one I've used
  - 1 x Breadboard
  - 1 x Extension cable (Suggested) to extend the GPIO ports of the Raspberry Pi and bring them closed to the breadboard
  - 10 x Jumper cables - Female (connect to Rasberry Pi GPIO) to Male (Connect to the Breadboard)
  - 1 x Tactile Push button
  - 1 x Raspberry Pi Cobbler board (Recommended, to breakout the GPIO's) and make working easier


Simple Motion sensor (PIR)
- This Simple Motion Sensor is a very simple program that detects the presence in a room using the PIR sensor and sets of an alarm 
- Components required include
  - 1 x Raspberry Pi 3 (I have used a 3, Model B. You can use whatever you have at your disposal.)
  - 1 x PIR Motion Sensor
    - https://littlebirdelectronics.com.au/products/pir-motion-sensor-module
    - http://www.dx.com/p/ir-infrared-motion-detection-sensor-module-dc-5v-20v-139624
    - http://www.dx.com/p/pyroelectric-infrared-pir-motion-sensor-detector-module-w-3-pin-cable-for-arduino-blue-white-397782 
  - 1 x Breadboard
  - 1 x Extension cable (Suggested) to extend the GPIO ports of the Raspberry Pi and bring them closed to the breadboard
  - 10 x Jumper cables - Female (connect to Rasberry Pi GPIO) to Male (Connect to the Breadboard)
  - 1 x Tactile Push button
  - 1 x Raspberry Pi Cobbler board (Recommended, to breakout the GPIO's) and make working easier


IoT - Read Analog Sensors using MCP 3008 & Upload data (Log to CSV and ThingSpeak/IoT Platform) 
- This program reads analog sensor values using an MCP 3008. An MCP 3008 is required since the Raspberry Pi does not have an ADC or Analog to Digital converter and is not in a position to read analog signals by itself.  
- Components required include
  - 1 x Raspberry Pi 3 (I have used a 3, Model B. You can use whatever you have at your disposal.)
  - 1 x PIR Motion Sensor
    - https://littlebirdelectronics.com.au/products/mcp3008-8-channel-10-bit-adc-with-spi-interface
  - 1 x Breadboard
  - 1 x Extension cable (Suggested) to extend the GPIO ports of the Raspberry Pi and bring them closed to the breadboard
  - 10 x Jumper cables - Female (connect to Rasberry Pi GPIO) to Male (Connect to the Breadboard)
  - 1 x Raspberry Pi Cobbler board (Recommended, to breakout the GPIO's) and make working easier
- To setup the project you will need to - 
  - Read through the tutorial at Adafruit -
    - https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi) 
  - Download and install the Adafruit libraries to interact with the MCP3008


Alexa on the Raspberry Pi 3
- Alexa as you know is Amazon's Voice service and now configurable on most maker platforms including the Raspberry Pi 3. This project is a fork of Sam Machin's code base including use of a tactile button and a single RGB LED.
- Components required include
  - 1 x Raspberry Pi 3 (I have used a 3, Model B. You can use whatever you have at your disposal.)
  - 1 x RGB LED 
    - https://tkkrlab.nl/wiki/Arduino_KY-016_3-color_LED_module
    - https://littlebirdelectronics.com.au/products/arduino-compatible-rgb-led-module
    - http://www.dx.com/p/diy-arduino-3-color-rgb-smd-led-module-black-135046
  - 1 x Breadboard
  - 1 x Extension cable (Suggested) to extend the GPIO ports of the Raspberry Pi and bring them closed to the breadboard
  - 10 x Jumper cables - Female (connect to Rasberry Pi GPIO) to Male (Connect to the Breadboard)
  - 1 x Tactile Push button
  - 1 x Raspberry Pi Cobbler board (Recommended, to breakout the GPIO's) and make working easier
- Code base can be obtained from the following github repository - https://github.com/tangowhisky37/AlexaPi
