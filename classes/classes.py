# creating basic classes for every element used

class Depot:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon



##########################################################################

class Plant:
    def __init__(self, name, lan, lon):
        self.name = name
        self.lon = lan
        self.lat = lon


##########################################################################

class Site:
    def __init__(self, zipcode, lon, lat):
        self.key = str(zipcode) + str(lon) + str(lat)
        self.zip = zipcode
        self.lon = lon
        self.lat = lat


##########################################################################

class Job:
    def __init__(self, id, key, plant, silo, material, start, duration, site):
        self.id = id
        self.key = key
        self.plant = plant
        self.silo = silo
        self.material = material
        self.start = start
        self.duration = duration
        self.site = site
