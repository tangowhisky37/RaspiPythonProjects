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

Mopidy (Audio Server) on the Raspberry Pi 3
- Mopidy is an extensible music server that plays music from local disk, Spotify, SoundCloud, Google Play Music, and more. You edit the playlist from any phone, tablet, or computer using a range of MPD and web clients. Head off to https://www.mopidy.com to learn more about the Mopidy music server.
- Let's step through the commands to download and install the base Mopidy player on your RaspberryPi
  - Download and install git on Raspbian using "sudo apt-get install git". This will install the git client on your RaspberryPi. You will need the git client to clone a lot of the repositories included in this tutorial.
  - Clone the github repository for Mopidy from https://github.com/mopidy/mopidy using "git clone https://github.com/mopidy/mopidy"
  - Change into downloaded Mopidy directory to build and install using the following commands, "sudo python setup.py install". This should build and install mopidy.
  - Clone the github repository for Mopidy-AlsaMixer from https://github.com/mopidy/mopidy-alsamixer using "git clone https://github.com/mopidy/mopidy-alsamixer"
  - Change into the downloaded mopidy-alsamixer directory to build and install using the following commands, "sudo python setup.py install". This should build and install mopidy-alsamixer.
- Now that we have installed Mopidy we need to review some of the other non-documented dependencies we will need to install. If we had not installed Mopidy from source (github) and rather installed Mopidy using the Raspbian packages (sudo apt-get install mopidy) the system would have auto resolved the dependencies.
- However, we've chosen not to install the stock packages since they are really outdated. We prefer the latest stable codebase from Github.
- Lets proceed now and manually install the following packages. These are part of the pre-requisites which i found missing and spent sometime/effort understanding what was required. The commands are - 
  - sudo apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
  - sudo apt-get install gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0
- You will now need to open up your Mopidy configuration file at /etc/mopidy/mopidy.conf and edit it to suit your requirements. For details on each of the configuration options please visit - https://docs.mopidy.com/en/latest/config/
- Please including configuration for the Mopidy AlsaMixer module into /etc/mopidy/mopidy.conf file. You can refer to a sample config at https://github.com/mopidy/mopidy-alsamixer
- Now that we've got this far we'll need to add the local repository to the configuration. See your [local] configuration section and add the location path to your music store. This one needs to be configured with a simple local unix path. 
- Start up Mopidy using "sudo /path/to/mopidy --config /etc/mopidy/mopidy.conf" and you should review the errors on the screen. Work through the errors. 
- Best case outcome would be that the only error is that the local plugin configuration has not found any files. Run the following command to initiate creation of a local cache, "sudo /path/to/mopidy --config /etc/mopidy/mopidy.conf local scan". This should run for a while depending on how much content you've got in your local music repository. I use my usb drive mounted on /mnt/usb0 and it took a while for Mopidy to scan through the content. 
- Once you've setup mopidy you should confirm if you are able to connect to the User Interface. Start mopidy with the command, "sudo /path/to/mopidy --config /etc/mopidy/mopidy.conf". Then connect to the user interface via a web browser  http://RaspberryPI_IP_Address_Here:6680/
- If you have the musicbox client installed you will see a link for it at the above page. Else you'll need to clone the git repository for Mopidy Musicbox Web client using "git clone https://github.com/pimusicbox/mopidy-musicbox-webclient"
  - Change into the downloaded mopidy-musicbox directory to build and install using the following commands, "sudo python setup.py install". This will build and install the mopidy-musicbox package onto the RaspberryPi.
  - Once you've installed mopidy music box you should confirm if you are able to connect to the User Interface. 
  - Start mopidy with the command, "sudo /path/to/mopidy --config /etc/mopidy/mopidy.conf".
  - Then connect to the user interface via a web browser  http://RaspberryPI_IP_Address_Here:6680/musicbox_webclient/index.html
- Check out these URL's if you are looking for Audio Streams to add to Musicbox
  - https://www.internet-radio.com/ 
  - http://www.australianliveradio.com/
  - http://www.listenlive.eu/jazz.html 
  - https://radio.abc.net.au/help/streams
- Obviously you might consider automating the startup of Mopidy. Like everything on unix/linux there's tons of ways of doing this. You could consider using daemon (daemontools) or simply /etc/rc.d/rc.local. Key in the startup command into rc.local and reboot the machine to find mopidy running in the background.
- Enjoy listening to your music!!!

Hacking the Disk Layout on a Raspberry Pi Model A 
- I've had some challenges building the Raspberry Pi A. I used the stock Raspbian distro on a 8 GB SDHC card. The default file system is around ~4GB in size with SWAP around ~128 MB in size.
- The updates ran really slow and i couldn't get any software loaded on it. So I decided to re-do the partitions and throw in some additinoal swap space. The memory on the device was 128MB with SWAP as 128 MB created part of the default install.
- The steps to extending the file system and creating a new one are as follows - 
  - Backup your system in case of a mistake!
  - Use "fdisk /dev/mmcblk0" to view your partitions. Note down the start and end sectors for your main partition.
  - Make sure you have cross checked and double cross checked the sector start/end information.
  - use fdisk to delete the partition, but do not reboot.
  - Recreate a new partition (similar type i.e. ext4 Linux) but with a larger size starting at the same location as the previous one. I extended mine by another 2 GB to give me a total of 6 GB.
  - Create a new SWAP file system. I gave mine ~1GB of space. 
  - Reboot to activate the partition changes. You should check "fdisk -l" to see the changes.
  - On rebooting use "resize2fs /dev/mmclk0p2" to enlarge the root Linux file system.
  - Some sites recommended using, "e2fsck -f /dev/mmcblk0p2" to perform a file system check. This however didn't work for me hence i used the next step.
  - If you perform the following, "touch /forcefsck" you will force an fsck at every boot. Just make sure you have the following entry in your /etc/fstav, "/dev/mmcblk0p2	/  ext4	defaults, noatime	0	1"
  - Create the new SWAP file system by using, "mkswap /dev/mmcblk0p3". 
  - Configure the /etc/fstab file with the following, "/dev/mmcblk0p3	swap	swap	defaults	0	0"
  - Reboot and you should see SWAP auto mounted. 
  - Links to read - 
    - https://www.raspberrypi.org/forums/viewtopic.php?f=51&t=45265
    - https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=86536
    - https://www.raspberrypi.org/forums/viewtopic.php?t=15870&p=884216
