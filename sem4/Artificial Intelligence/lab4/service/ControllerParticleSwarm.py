from PyQt5.QtCore import QThread
from PyQt5 import QtCore
from domain.State import State


class ControllerParticleSwarm(QThread):
    CURRENT_BEST = QtCore.pyqtSignal(str)

    def __init__(self, problem, maxIterations, swarmSize):
        super(ControllerParticleSwarm, self).__init__()

        self.problem = problem
        self.maxIterations = maxIterations
        self.swarmSize = swarmSize

        self.running = False

        self.swarm = self.problem.createPopulation(self.swarmSize)
        self.currentIteration = 0
        
    def run(self):
        self.running = True

        while self.running and self.currentIteration < self.maxIterations:
            self.currentIteration += 1
            swarm = self.problem.iteration(self.swarm)
            values = self.problem.toMatrix(swarm[0].getPosition())

            self.CURRENT_BEST.emit(str(State(values)) + "Current iteration: " + str(self.currentIteration) + "\n")

        self.running = False

    def getRunningStatus(self):
        return self.running

    def setRunningStatus(self, running):
        self.running = running

    def runStatistic(self):
        stats = []
        bestFitness = 100000
        while self.currentIteration < self.maxIterations:
            self.currentIteration += 1
            swarm = self.problem.iteration(self.swarm)

            fitness = self.problem.fitness(swarm[0].getPosition())

            if bestFitness > fitness:
                bestFitness = fitness
                stats.append(bestFitness)

        return stats
