import random

class Jump(object):

    def __init__(self, name, timeInAir, avgSpeed, windVelocity):
        self.__name = name
        self.__timeInAir = timeInAir
        self.__avgSpeed = avgSpeed
        self.__windVelocity = windVelocity
        self.__distance = timeInAir *( avgSpeed + avgSpeed * random.uniform(-0.5, 0.5) + windVelocity )


    def getName(self):
        return self.__name

    def getTimeInAir(self):
        return self.__timeInAir

    def getAvgSpeed(self):
        return self.__avgSpeed

    def getWindVelocity(self):
        return self.__WindVelocity

    def getDistance(self):
        return self.__distance



    def setName(self, new):
        self.__name = new

    def setTimeInAir(self, new):
        self.__timeInAir = new

    def setAvgSpeed(self, new):
        self.__avgSpeed = new

    def setWindVelocity(self, new):
        self.__windVelocity = new

    def setDistance(self):
        return self.__distance

    def __str__(self):
        return str(self.__name) + " - " + str(round(self.__distance))
