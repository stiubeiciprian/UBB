from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from algorithms.ProblemParticleSwarmOptimisation import ProblemParticleSwarmOptimisation
from service.ControllerParticleSwarm import ControllerParticleSwarm


class PSOWindow(QMainWindow):
    def __init__(self):
        super(PSOWindow, self).__init__()
        uic.loadUi("E:/Projects/Lab3/ui/windows/PSOWindow.ui", self)

        self.running = False
        self.problem = None
        self.cont = None

        stopButton = self.findChild(QtWidgets.QPushButton, 'buttonStop')
        stopButton.clicked.connect(self.stop)

        stopButton = self.findChild(QtWidgets.QPushButton, 'buttonStart')
        stopButton.clicked.connect(self.start)

        self.inputSquareSize = self.findChild(QtWidgets.QLineEdit, 'lineEditSquareSize')
        self.inputIterationsNumber = self.findChild(QtWidgets.QLineEdit, 'lineEditIterationNumber')
        self.inputSwarmSize = self.findChild(QtWidgets.QLineEdit, 'lineEditSwarmSize')

        self.output = self.findChild(QtWidgets.QTextEdit, 'textEditResult')

        self.show()

    def stop(self):
        self.cont.setRunningStatus(False)

    def start(self):
        problemSize = int(self.inputSquareSize.text())
        iterations = int(self.inputIterationsNumber.text())
        swarmSize = int(self.inputSwarmSize.text())

        self.problem = ProblemParticleSwarmOptimisation(problemSize)
        self.cont = ControllerParticleSwarm(self.problem, iterations, swarmSize)
        self.cont.CURRENT_BEST.connect(self.setOutput)
        self.cont.start()

    @pyqtSlot(str)
    def setOutput(self, node):
        self.output.clear()
        outputStr = "\nCurrent Best:" + node
        self.output.append(outputStr)
