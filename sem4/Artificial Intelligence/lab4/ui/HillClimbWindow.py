from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from algorithms.ProblemHillClimbing import ProblemHillClimbing
from service.ControllerHillClimbing import ControllerHillClimbing
from PyQt5.QtCore import pyqtSlot


class HillClimbWindow(QMainWindow):
    def __init__(self):
        super(HillClimbWindow, self).__init__()
        uic.loadUi("E:/Projects/Lab3/ui/windows/HillClimbWindow.ui", self)

        self.running = False
        self.problem = None
        self.cont = None

        self.stopButton = self.findChild(QtWidgets.QPushButton, 'buttonStop')
        self.stopButton.clicked.connect(self.stop)
        self.startButton = self.findChild(QtWidgets.QPushButton, 'buttonStart')
        self.startButton.clicked.connect(self.start)

        self.inputSquareSize = self.findChild(QtWidgets.QLineEdit, 'lineEditSquareSize')
        self.inputIterationsNumber = self.findChild(QtWidgets.QLineEdit, 'lineEditIterationNumber')

        self.output = self.findChild(QtWidgets.QTextEdit, 'textEditResult')

        self.show()

    def stop(self):
        self.cont.setRunningStatus(False)

    def start(self):
        problemSize = int(self.inputSquareSize.text())
        iterations = int(self.inputIterationsNumber.text())

        self.problem = ProblemHillClimbing(problemSize)
        self.cont = ControllerHillClimbing(self.problem, iterations)

        self.cont.CURRENT_BEST.connect(self.setOutput)

        self.cont.start()

    @pyqtSlot(str)
    def setOutput(self, node):
        self.output.clear()
        outputStr = "\nCurrent Best:" + node
        self.output.append(outputStr)
