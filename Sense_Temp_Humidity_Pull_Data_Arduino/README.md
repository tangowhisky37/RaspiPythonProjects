Weather Reporting using OWM (https://github.com/tangowhisky37/RaspiPythonProjects/tree/master/Sense_Temp_Humidity_Pull_Data_Arduino) 
- While the Sense_Temp_Humidity project (above) was designed as a simple IoT (Internet Of Things) project to pull data from my DHT11 on the Raspberry Pi to be uploaded to ThingSpeak, Weather Reporting on the other hand pulls data from OpenWeatherMap and uploads the data to Thingspeak.
- The objective of this project was to be able to compare the data for temperature, humidity being collected by my sensors at home with the data for the city i live in provided by Open Weather Map.
- The project uses the Open Weather Map python library which you will need to download and install on the Raspberry Pi
- This project has evolved to log data to CSV including upload of data to the ThingSpeak/IoT Platform
- Components required include - 
 - Python module for OWM from https://github.com/csparpa/pyowm
 - 1 x Raspberry Pi 3 (I have used a 3, Model B. You can use whatever you have at your disposal.
