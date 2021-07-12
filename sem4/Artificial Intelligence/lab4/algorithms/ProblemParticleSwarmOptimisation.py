from domain.Particle import Particle
import random
import numpy as np
import itertools


class ProblemParticleSwarmOptimisation:
    def __init__(self, n):
        self.n = n
        self.coordinates = np.asarray(list(itertools.permutations(list(range(1, self.n+1)))))
        self.coordinatesLength = len(self.coordinates)

        self.inertiaCoefficient = 0.5
        self.cognitiveLearningCoefficient = 2
        self.socialLearningCoefficient = 1.5

    def getCoordinates(self):
        return self.coordinates

    def createIndividual(self):
        position = np.random.randint(0, self.coordinatesLength, size=self.n*2)
        return Particle(position, self.fitness(position))

    def toMatrix(self, position):
        individual = []
        for i in position:
            individual.append(list(self.coordinates[i]))

        return individual

    def createPopulation(self, size):
        return [self.createIndividual() for i in range(size)]

    def fitness(self, position):
        individual = self.toMatrix(position)

        score = 0
        s = self.n * (self.n + 1) / 2

        for col in range(self.n):
            colSum1, colSum2 = 0, 0
            for row in range(self.n):
                colSum1 += individual[row][col]
                colSum2 += individual[row + self.n][col]

            score += 1 if colSum1 != s else 0
            score += 1 if colSum2 != s else 0

        for row in range(self.n):
            for col in range(self.n):
                for i in range(self.n):
                    for j in range(self.n):
                        if (row != i or col != j) and individual[row][col] == individual[i][j] and \
                                individual[row + self.n][col] == individual[i + self.n][j]:
                            score += 1
        return score

    def selectBestNeighbour(self, particle, population):
        neighbours = []

        for neighbour in population:
            if neighbour != particle:
                neighbours.append(neighbour)

        random.shuffle(neighbours)
        bestNeighbours = sorted(neighbours[:len(population)//3], key=lambda p: self.fitness(p.getPosition()))

        return bestNeighbours[0]

    def getParticleNewVelocity(self, particle, population):
        result = np.zeros(self.n*2)

        # Force the particle to move in the same position it moved until now
        currentVelocity = particle.getVelocity()
        velocity = self.inertiaCoefficient * currentVelocity

        result += velocity

        # Force the particle to move towards its best position
        currentPosition = particle.getPosition()
        bestPosition = particle.getBestPosition()
        cognitiveFactor = self.cognitiveLearningCoefficient * random.random() * (bestPosition - currentPosition)

        result += cognitiveFactor

        # Force the particle to move towards the best position found by neighbours
        bestNeighbour = self.selectBestNeighbour(particle, population)
        bestNeighbourPosition = bestNeighbour.getPosition()
        socialFactor = self.socialLearningCoefficient * random.random() * (bestNeighbourPosition - currentPosition)

        result += socialFactor

        return result.astype(np.int8)

    def iteration(self, population):
        for particle in population:
            velocity = self.getParticleNewVelocity(particle, population)
            particle.setVelocity(velocity)

            newPosition = np.clip(particle.getPosition() + velocity, a_min=0, a_max=self.coordinatesLength-1)
            newFitness = self.fitness(newPosition)

            particle.updatePosition(newPosition, newFitness)

        return sorted(population, key=lambda p: self.fitness(p.getPosition()))
