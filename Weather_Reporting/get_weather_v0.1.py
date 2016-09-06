#!/usr/bin/python

import pyowm

owm = pyowm.OWM('2866c7dec86f0ad873d0f626dafcd20e')  # You MUST provide a valid API key
#owm.set_API_key('2866c7dec86f0ad873d0f626dafcd20e')

# You have a pro subscription? Use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
#forecast = owm.daily_forecast("Milan,it")
#tomorrow = pyowm.timeutils.tomorrow()
#forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
#observation = owm.weather_at_place('London,uk')
observation = owm.weather_at_place('Melbourne,au')
w = observation.get_weather()
#print(w)                      # <Weather - reference time=2013-12-18 09:20, 
                              # status=Clouds>

# Weather details
print(w.get_wind())                  # {'speed': 4.6, 'deg': 330}
print(w.get_humidity())              # 87
print(w.get_temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#print(w)                      # <Weather - reference time=2013-12-18 09:20, 

# Search current weather observations in the surroundings of 
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)
