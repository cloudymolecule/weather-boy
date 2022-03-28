from opencage.geocoder import OpenCageGeocode

class Geolocator():
    def __init__(self, query):
        self.api = self._open_file('api_key.txt')
        self.query = query
        self.data = self._get_data()

    def _get_data(self):
        geocoder = OpenCageGeocode(self.api)
        data = geocoder.geocode(self.query)
        if len(data) == 0:
            self.stat = 400
            return data
        else:
            self.stat = 200
            self.coordinates = data[0]['geometry']
            self.flag = data[0]['annotations']['flag']
            self.location_data = data[0]['components']
            return data[0]
    
    def _open_file(self, file):
        f = open(file, 'r')
        return f.read()
