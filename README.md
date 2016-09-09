# RaspiPythonProjects

This folder contains a list of all the Raspberry Pi projects I have been working on

BlinkLEDs
- This folder includes programs that uses the Raspberry Pi's GPIO pins to interact with multiple LED's
- This folder also includes programs that use the Raspberry Pi's GPIO pins to interact with a simple push button
- Components required for the programs in this folder include 
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

Sense_Temp_Humidity (Log to CSV and ThingSpeak/IoT Platform)
- Components required for the programs in this folder include
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

Simple light sensor 
- This is a very simple program that detects the presence of light or darkness
- Components required include 
  - 1 x Photoresistor Light Sensor module
    - http://www.buildcircuit.com.au/Photoresistor-Sensor-Module-Light-Detection-for-arduino
    - http://www.dx.com/p/6495-photoresistor-light-sensor-module-for-smart-car-black-blue-152774#.V9KBmZh97IU
    - https://tkkrlab.nl/wiki/Arduino_KY-018_Photo_resistor_module 
   - The first two links very closely resemble the one I've used
