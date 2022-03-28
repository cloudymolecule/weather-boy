import os
from lib.weather import Weather
from lib.space import Space
from lib.geolocator import Geolocator

class CommandLineInterface():
    def __init__(self):
        self.running = True
        self.space = Space()
    
    # clears screen when called
    def _clear_screen(self):
        os.system('clear')

    # starts the cli
    def run_program(self):
        self._clear_screen()
        self.greeting()

        while self.running:
            location = input('What location do you want to check the weather for?: ')
            g = Geolocator(location) # Geolocator class instance
            while g.stat != 200:
                print('Location not found, please try again.')
                location = input('What location do you want to check the weather for?: ')
                g = Geolocator(location) # Another instance in case input didn't match a place

            w = Weather(latitude= g.coordinates['lat'], longitude= g.coordinates['lng'])
            self.location_display(g.coordinates, g.flag, g.data)

            selection = None # no selections yet, just setting it up for while loop that menu uses
            
            while selection not in ['Q']:
                selection = self.menu()
                self._clear_screen()
                if selection == 'C':
                    self.location_display(g.coordinates, g.flag, g.data)
                    w.current()
                elif selection == 'W':
                    w.week()
                elif selection == 'H':
                    w.hourly()
                elif selection == 'O':
                    self.running = False
                    return 'Another'
                elif selection == 'A':
                    self.space.displayAstronauts()
                elif selection == 'Q':
                    self.bye()
                    self.running = False
                    return 'Done'

    # friendly greeting
    def greeting(self):
        print('Howdy there friend!\n')

    # user makes a choice
    def menu(self):
        menu_str = 'Type "C" to get the current weather forecast.\nType "W" to get the forecast for the week.\nType "H" to see the hourly forecast.\nType "O" to see another location.\nType "A" to see how many astronauts are currently in space.\nType "Q" to quit.'
        print(menu_str)
        inp = input('What will it be?: ').upper()
        print(inp)
        while inp not in ['C', 'W', 'H', 'O', 'A', 'Q']:
            self._clear_screen()
            print('Incorrect, please try again.')
            print(menu_str)
            inp = input('What will it be?: ').upper()
        return inp

    # bye!
    def bye(self):
        print('Goodbye! See you again soon!')

    # displays info aboout selected location
    def location_display(self, coordinates, flag, data):
        formatted_loc = data['formatted']
        continent = data['components']['continent']
        lat = coordinates['lat']
        lng = coordinates['lng']

        print(f'Current coordinates for {formatted_loc} {flag}\nlocated in the continent of {continent}\nlatitude: {lat}\tlongitude: {lng}\n')
