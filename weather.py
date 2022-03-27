import os
import json
import requests
import calendar
# from datetime import datetime

class Weather:

    def __init__(self, latitude=40.3, longitude=-75.1):
        self.coordinates = {latitude, longitude}
        self.url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,apparent_temperature,precipitation,windspeed_10m,winddirection_10m,windgusts_10m&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York'
        self.data = self.__getWeather__()
        # self.current_weather = self.data['current_weather']
    
    def __getWeather__(self):
        request = requests.get(self.url)
        response = request.json()
        return response

    def current(self):
        date, time = self.data['current_weather']['time'].split('T')
        date = date.split('-')
        year = date[0]
        month = calendar.month_name[int(date[1])]
        day = date[2]
        temperature = self.data['current_weather']['temperature']
        windspeed = self.data['current_weather']['windspeed']

        def getWeatherInterpretation(weathercode):
            match weathercode:
                case 0: 
                    return 'clear sky'
                case 1: 
                    return 'mainly clear' 
                case 2:
                    return 'partly cloudy'
                case 3:
                    return 'overcast'
                case 45: 
                    return 'fog'
                case 48: 
                    return 'depositing rime fog'
                case 51: 
                    return 'light drizzle'
                case 53:
                    return 'moderate drizzle'
                case 55: 
                    return 'dense drizzle'
                case 56:  
                    return 'light intensity freezing drizzle'
                case 57:
                    return 'dense intensity freezing drizzle'
                case 61:  
                    return 'slight intensity rain'
                case 63:
                    return 'moderate intesity rain'
                case 65:
                    return 'heavy intensity rain'
                case 66: 
                    return 'light intensity freezing rain'
                case 67:
                    return 'heavy intensity freezing rain'
                case 71: 
                    return 'slight intensity snow fall'
                case 73:
                    return 'moderate intensity snow fall'
                case 75:
                    return 'heavy intensity snow fall'
                case 77: 
                    return 'snow grains'
                case 80: 
                    return 'slight rain showers'
                case 81:
                    return 'moderate rain showers'
                case 82:
                    return 'violent rain showers'
                case 85: 
                    return 'slight snow showers'
                case 86:
                    return 'heavy snow showers'
                case 95: 
                    return 'moderate thunderstorm'
                case 96: 
                    return 'thunderstorm with slight hail'
                case 99:
                    return 'thunderstorm with heavy hail'

        weather_interpretation = getWeatherInterpretation(int(self.data['current_weather']['weathercode']))
            
        def windDirection(degrees):
            match degrees:
                case degrees if degrees >= 350 and degrees <= 360 or degrees <= 19:
                    return 'North (N)'
                case degrees if degrees >= 20 and degrees <= 39:
                    return 'North-northeast (N/NE)'
                case degrees if degrees >= 40 and degrees <= 59:
                    return 'Northeast (NE)'
                case degrees if degrees >= 60 and degrees <= 79:
                    return 'East-northeast (E/NE)'
                case degrees if degrees >= 80 and degrees <= 109:
                    return 'East (E)'
                case degrees if degrees >= 110 and degrees <= 129:
                    return 'East-southeast (E/SE)'
                case degrees if degrees >= 130 and degrees <= 149:
                    return 'Southeast (SE)'
                case degrees if degrees >= 150 and degrees <= 169:
                    return 'South-southeast (S/SE)'
                case degrees if degrees >= 170 and degrees <= 199:
                    return 'South (S)'
                case degrees if degrees >= 200 and degrees <= 219:
                    return 'South-southwest (S/SW)'
                case degrees if degrees >= 220 and degrees <= 239:
                    return 'Southwest (SW)'
                case degrees if degrees >= 240 and degrees <= 259:
                    return 'West-southwest (W/SW)'
                case degrees if degrees >= 260 and degrees <= 289:
                    return 'West (W)'
                case degrees if degrees >= 290 and degrees <= 309:
                    return 'West-northwest (W/NW)'
                case degrees if degrees >= 310 and degrees <= 329:
                    return 'Northwest (NW)'
                case degrees if degrees >= 330 and degrees <= 349:
                    return 'North-northwest (N/NW)'


        return f'Today is {month} {day}, {year}.\nThe current weather condition is {weather_interpretation} with a temperature of {temperature}°F\nCurrent windspeed is {windspeed} Mph'
        
w = Weather(40.3, -75.1)

print(w.current())