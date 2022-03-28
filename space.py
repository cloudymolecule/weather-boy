import requests
import calendar
from time import sleep

class Space:
    def __init__(self):
        self.url = 'http://api.open-notify.org/astros.json'
        self.data = self._getAstronauts(self.url)
        self.astronauts = self.data['people']
        self.astronauts_count = len(self.data['people'])
    
         # this adjusts the 'sleep' and the way it displays
        self.display_speed = 0.05

    def _getAstronauts(self, url):
        request = requests.get(self.url)
        response = request.json()
        return response

    def displayAstronauts(self):
        
        legends = [f'There are currently {self.astronauts_count} astronauts in space, here are the names of these brave humans:\n']

        for num in range(0, self.astronauts_count):
            
            astro = f"{self.astronauts[num]['name']} currently in the |{self.astronauts[num]['craft']}| spacecraft.\n"
            
            legends.append(astro)
        

        for num in legends:
            sleep(self.display_speed)
            print(num)
            
       