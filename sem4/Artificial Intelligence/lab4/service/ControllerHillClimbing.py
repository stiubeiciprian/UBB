from PyQt5.QtCore import QThread
from PyQt5 import QtCore
from domain.State import State


class ControllerHillClimbing(QThread):
    CURRENT_BEST = QtCore.pyqtSignal(str)

    def __init__(self, problem, maxIterations):
        super(ControllerHillClimbing, self).__init__()

        self.problem = problem
        self.maxIterations = maxIterations
        self.running = False

        self.currentNode = self.problem.generateStartingPoint()
        self.currentIteration = 0

    def run(self):
        self.running = True
        while self.running and self.currentIteration < self.maxIterations:
            nextNode = self.problem.iteration(self.currentNode)

            if nextNode == self.currentNode:
                self.CURRENT_BEST.emit(str(State(nextNode)) + "Current iteration: " + str(self.currentIteration) + "\n")
                self.running = False
                return
            
            self.currentIteration += 1
            self.currentNode = nextNode
            self.CURRENT_BEST.emit(str(State(self.currentNode)) + "Current iteration: " + str(self.currentIteration) + "\n")
        self.running = False

    def getRunningStatus(self):
        return self.running

    def setRunningStatus(self, running):
        self.running = running
