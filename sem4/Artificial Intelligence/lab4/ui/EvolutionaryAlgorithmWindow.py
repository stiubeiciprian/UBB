from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from algorithms.ProblemEvolutionaryAlgorithm import ProblemEvolutionaryAlgorithm
from service.ControllerEvolutionary import ControllerEvolutionary
from domain.State import State



class EvolutionaryAlgorithmWindow(QMainWindow):
    def __init__(self):
        super(EvolutionaryAlgorithmWindow, self).__init__()
        uic.loadUi("E:/Projects/Lab3/ui/windows/EvolutionaryWindow.ui", self)

        self.running = False

        self.problem = None
        self.cont = None

        stopButton = self.findChild(QtWidgets.QPushButton, 'buttonStop')
        stopButton.clicked.connect(self.stop)

        startButton = self.findChild(QtWidgets.QPushButton, 'buttonStart')
        startButton.clicked.connect(self.start)

        self.inputSquareSize = self.findChild(QtWidgets.QLineEdit, 'lineEditSquareSize')
        self.inputIterationsNumber = self.findChild(QtWidgets.QLineEdit, 'lineEditIterationNumber')
        self.inputProbability = self.findChild(QtWidgets.QLineEdit, 'lineEditProbability')
        self.inputPopulationSize = self.findChild(QtWidgets.QLineEdit, 'lineEditPopulationSize')

        self.output = self.findChild(QtWidgets.QTextEdit, 'textEditResult')

        self.show()

    def stop(self):
        self.cont.setRunningStatus(False)

    def start(self):
        problemSize = int(self.inputSquareSize.text())
        maxIterations = int(self.inputIterationsNumber.text())
        populationSize = int(self.inputPopulationSize.text())
        probability = float(self.inputProbability.text())

        self.problem = ProblemEvolutionaryAlgorithm(problemSize)
        self.cont = ControllerEvolutionary(self.problem, populationSize, probability, maxIterations)

        self.cont.CURRENT_BEST.connect(self.setOutput)

        self.cont.start()


    def setOutput(self, node):
        self.output.clear()
        outputStr = "Current Best:\n" + node
        self.output.append(outputStr)
