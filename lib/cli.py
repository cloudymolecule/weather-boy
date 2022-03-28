import os
from lib.weather import Weather
from lib.space import Space

class CommandLineInterface():
    def __init__(self):
        self.running = True
        # self.weather = Weather(40.3, -75.1)
        self.space = Space()
    
    def _clear_screen(self):
        os.system('clear')

    
    def run_program(self):


        # wea = Weather(40.3, -75.1)
        self._clear_screen()
        self.greeting()

        while self.running:
            location = input('Where are you? ')
            self.running = False

        # wea.current()
        # print('')
        # wea.week()
        # print('')
        # wea.hourly()
        # print('')
        # self.space.displayAstronauts()

    def check_coordinates(self, coor):
        pass

    def greeting(self):
        print('Howdy there friend!')