import os
from lib.weather import Weather
from lib.space import Space
from lib.geolocator import Geolocator
from colorama import Fore, Back, Style

class CommandLineInterface():
    def __init__(self):
        self.running = True
        self.space = Space() # Space class instance
    
    # clears screen when called
    def _clear_screen(self):
        os.system('clear')

    # starts the cli
    def run_program(self):
        self._clear_screen()
        self.greeting()

        while self.running:
            location = input(Fore.YELLOW + Style.BRIGHT + 'What location do you want to check the weather for?: ' + Style.RESET_ALL)
            g = Geolocator(location) # Geolocator class instance
            while g.stat != 200:
                print(Fore.RED + Style.BRIGHT + 'Location not found, please try again.' + Style.RESET_ALL)
                location = input(Fore.YELLOW + Style.BRIGHT + 'What location do you want to check the weather for?: ' + Style.RESET_ALL)
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
        print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + 'Howdy there friend!\n' + Style.RESET_ALL)

    # user makes a choice
    def menu(self):
        menu_str = Fore.CYAN + 'Type "C" to get the current weather forecast\nType "W" to get the forecast for the week\nType "H" to see the hourly forecast\nType "O" to see another location\nType "A" to see how many astronauts are currently in space\nType "Q" to quit\n' + Style.RESET_ALL
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
        print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + 'Goodbye! See you again soon!' + Style.RESET_ALL)

    # displays info aboout selected location
    def location_display(self, coordinates, flag, data):
        formatted_loc = data['formatted']
        continent = data['components']['continent']
        lat = coordinates['lat']
        lng = coordinates['lng']

        print(f'Current coordinates for {formatted_loc} {flag}\nlocated in the continent of {continent}\n'+ Fore.WHITE + Back.YELLOW + Style.BRIGHT +f'latitude: {lat}\tlongitude: {lng}\n' + Style.RESET_ALL)
