# Weather Boy

## Description

The name actualy comes from here: [https://www.youtube.com/watch?v=XOi2jFIhZhA] <br />
Weather Boy is a weather app that does a lot, it:
1. Provides a current forecast
2. Provides a forecast for the next 7 days
3. Gives you an hourly forecast for 7 days (you better have a well-oiled mouse wheel)
4. Allows you to see how many astronautas are currently in space

## How to install and run

* Clone and fork this repository, double check Python is installed in your system
* Make sure you have the few dependencies I've used, if not just install them

pip3 install colorama<br />
pip3 install opencage<br />
pip3 install requests<br />

## How to use

<p>From the weather-boy directory type:</p> 

**python3 start.py**

The first thing you'll do is select a location, the most descriptive the better; I've found the Opencage API to be awesome at matching places.<br />
So for example you could type:
*Philadelphia, PA*
It'll show you more info. Depending on how precise the location, the county, the zip code and the country's flag.

From there just select an item from the menu and press enter

**Here's the menu**

Type "C" to get the current weather forecast<br />
Type "W" to get the forecast for the week<br />
Type "H" to see the hourly forecast<br />
Type "O" to see another location<br />
Type "A" to see how many astronauts are currently in space<br />
Type "Q" to quit<br />

## APIs

I've utilized 3 API's in this project, and here they are in order of appearance<br />

Pretty cool API, tells you how many people are currently in space<br />
People In Space http://open-notify.org/Open-Notify-API/People-In-Space/

Allows me to send convert a location string and receive location data including coordinates<br />
Opencage https://opencagedata.com/

Passing the coordinates from Opencage I can get local weather info<br />
Open-Meteo https://open-meteo.com/en

## Credits
Everyone involved in creating and maintaining these amazing free APIs so developers like me can learn and create.