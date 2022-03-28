import os
from lib.weather import Weather
from lib.space import Space
from lib.geolocator import Geolocator
from pprint import pprint

class CommandLineInterface():
    def __init__(self):
        self.running = True
        self.space = Space()
    
    def _clear_screen(self):
        os.system('clear')

    
    def run_program(self):
        self._clear_screen()
        self.greeting()

        while self.running:
            location = input('What location do you want to check the weather for?: ')
            g = Geolocator(location)

            # w = Weather(latitude= g.coordinates['lat'], longitude= g.coordinates['lng'])
            # self.location_display(g.coordinates, g.flag, g.data)
            
            
            
            # w.current()
            # print('')
            # w.week()
            # print('')
            # w.hourly()
            # print('')
            # self.space.displayAstronauts()
            self.running = False

    def greeting(self):
        print('Howdy there friend!')

    def bye(self):
        print('bye')

    def input_check(self, inp):
        return inp.isalpha()

    def location_display(self, coordinates, flag, data):
        formatted_loc = data['formatted']
        continent = data['components']['continent']
        lat = coordinates['lat']
        lng = coordinates['lng']

        print(f'Current coordinates for {formatted_loc} {flag}\nlocated in the continent of {continent}\nlatitude: {lat}\tlongitude: {lng}')
