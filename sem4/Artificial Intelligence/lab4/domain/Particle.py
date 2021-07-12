import numpy as np


class Particle:
    def __init__(self, position, fitness):
        self.position = position
        self.bestPosition = position
        self.bestFitness = fitness
        self.n = len(self.position) // 2
        self.velocity = np.zeros(self.n * 2, dtype=np.int8)

    def updatePosition(self, newPosition, newFitness):
        if newFitness < self.bestFitness:
            self.bestPosition = newPosition
            self.bestFitness = newFitness

        self.position = newPosition

    def getPosition(self):
        return self.position

    def getBestPosition(self):
        return self.bestPosition

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, newVelocity):
        self.velocity = newVelocity

    def getBestFitness(self):
        return self.bestFitness
