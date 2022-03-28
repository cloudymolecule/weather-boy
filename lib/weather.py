import requests
import calendar
from time import sleep
from datetime import datetime

class Weather:
    def __init__(self, latitude=40.71, longitude=-74.01): # defaults to NYC
        self.coordinates = {latitude, longitude}
        self.url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,apparent_temperature,precipitation,windspeed_10m,winddirection_10m,windgusts_10m&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York'
        self.data = self._get_weather()
        
        # this adjusts the 'sleep' and the way it displays
        self.display_speed = 0.01

    def _get_weather(self):
        request = requests.get(self.url)
        response = request.json()
        return response

    def current(self):
        date = self._format_time('d', self.data['current_weather']['time'])
        time = self._format_time('t', self.data['current_weather']['time'])
        local_time = datetime.now().strftime('%H:%M')
        year = date[0]
        month = calendar.month_name[int(date[1])]
        day = date[2]
        temperature = self.data['current_weather']['temperature']
        windspeed = int(self.data['current_weather']['windspeed'])
        wind_degrees = self.data['current_weather']['winddirection']
        elevation = self.data['elevation']

        weather_interpretation = self._get_weather_interpretation(int(self.data['current_weather']['weathercode']))

        wind_direction = self._get_wind_direction(windspeed)

        print (f'Today is {month} {day}, {year} and the time is {local_time}. This forecast was prepared at {time}.\nThe current weather condition is {weather_interpretation} with a temperature of {temperature}°F ({self._convert_from_f_to_c(temperature)}°C)\nCurrent windspeed is {windspeed} Mph with a {wind_degrees}°, {wind_direction} direction as the crow flies.\nElevation at location is {self._convert_meters_to_feet(elevation)} feet ({elevation} meters) above sea level.\n')
        
    def week(self):
        w_weathercodes = self.data['daily']['weathercode']
        w_dates = self.data['daily']['time']
        w_sunrises = self.data['daily']['sunrise']
        w_sunsets = self.data['daily']['sunset']
        w_min_temps = self.data['daily']['temperature_2m_min']
        w_max_temps = self.data['daily']['temperature_2m_max']
        
        all_week = ["Here's your forecast for the week:\n"]
        
        for num in range(0, 7):
            date = self._format_time('d_only', w_dates[num])
            year = date[0]
            month = calendar.month_name[int(date[1])]
            day = date[2]

            sunrise = self._format_time('t', w_sunrises[num])
            sunset = self._format_time('t', w_sunsets[num])
            min_temp = w_min_temps[num]
            max_temp = w_max_temps[num]
            weather_interpretation = self._get_weather_interpretation(int(w_weathercodes[num]))            

            forecast = f'On {month} {day}, {year} the weather condition will be {weather_interpretation}\nsunrise will be at {sunrise} and sunset will be at {sunset}\nthe minimum temperature will be {min_temp}°F ({self._convert_from_f_to_c(min_temp)}°C),\nand the maximum temperature will be {max_temp}°F ({self._convert_from_f_to_c(max_temp)}°C)\n'
            all_week.append(forecast)


        for day in all_week:
            sleep(self.display_speed)
            print(day) 

    def hourly(self):
        h_temp = self.data['hourly']['temperature_2m']
        h_wind_dir = self.data['hourly']['winddirection_10m']
        h_precipitation = self.data['hourly']['precipitation']
        h_time = self.data['hourly']['time']
        h_winds = self.data['hourly']['windspeed_10m']
        h_appt_temp = self.data['hourly']['apparent_temperature']
        h_gusts = self.data['hourly']['windgusts_10m']

        all_hours = ['Hourly forecast for the next 7 days:\n']

        for num in range(0,len(h_time)):
            date = self._format_time('d', h_time[num])
            time = self._format_time('t', h_time[num])
            year = date[0]
            month = calendar.month_name[int(date[1])]
            day = date[2]
            wind_direction = self._get_wind_direction(h_wind_dir[num])

            forecast = f'Hourly forecast for {month} {day}, {year} at {time}:\nTemperature {h_temp[num]}°F ({self._convert_from_f_to_c(h_temp[num])}°C)\tApparent temperature {h_appt_temp[num]}°F ({self._convert_from_f_to_c(h_appt_temp[num])}°C)\nWindspeed {h_winds[num]} Mph\tWind direction {h_wind_dir[num]}° {wind_direction}\nWind gusts {h_gusts[num]} Mph\tPrecipitation {h_precipitation[num]}"\n'
            
            all_hours.append(forecast)
            
        for hour in all_hours:
            sleep(self.display_speed)
            print(hour)

    def _format_time(self, type, time):
        if type == 'd_only':
            return time.split('-') # in this case it's date actually, hence the 'd_only'
        if type == 'd':
            date_and_time = time.split('T')
            return date_and_time[0].split('-')
        elif type == 't':
            date_and_time = time.split('T')
            return date_and_time[1]
        else:
            return 'Impossible, there is an awful error'

    def _convert_meters_to_feet(self, meters):
        return round((meters* 3.28084), 2)
    def _convert_from_f_to_c(self, temp):
        return round((temp - 32) * (5/9), 1)

    def _get_weather_interpretation(self, weathercode):
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
                return 'moderate thunderstorms'
            case 96: 
                return 'thunderstorm with slight hail'
            case 99:
                return 'thunderstorm with heavy hail'
    
    def _get_wind_direction(self, degrees):
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

