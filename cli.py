import os
from weather import Weather
from space import Space

w = Weather(40.3, -75.1)

s = Space()

os.system('clear')

print('Howdy there friend!\n')

w.current()
print('')
w.week()
print('')
w.hourly()
print('')
s.displayAstronauts()