from PyQt5.QtCore import QThread
from PyQt5 import QtCore
from domain.State import State


class ControllerEvolutionary(QThread):
    CURRENT_BEST = QtCore.pyqtSignal(str)

    def __init__(self, problem, populationSize, probability, maxIterations):
        super(ControllerEvolutionary, self).__init__()

        self.problem = problem
        self.populationSize = populationSize
        self.maxIterations = maxIterations
        self.probability = probability
        self.running = False

        self.currentGeneration = self.problem.createPopulation(self.populationSize)
        self.currentIteration = 0

    def run(self):
        self.running = True
        while self.running and self.currentIteration < self.maxIterations:
            nextGeneration = self.problem.iteration(self.currentGeneration, self.populationSize, self.probability)
            self.currentIteration += 1
            self.currentGeneration = nextGeneration
            self.CURRENT_BEST.emit(str(State(self.currentGeneration[0])) + "Current iteration: " + str(self.currentIteration) + "\n")

        self.running = False

    def getRunningStatus(self):
        return self.running

    def setRunningStatus(self, running):
        self.running = running
