from opencage.geocoder import OpenCageGeocode

class Geolocator():
    def __init__(self):
        self.api = self._open_file('api_key.txt')

    def find_coordinates(self, query):
        geocoder = OpenCageGeocode(self.api)
        return geocoder.geocode(query)

    def _open_file(self, file):
        f = open(file, 'r')
        return f.read()

