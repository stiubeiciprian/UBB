from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ui.EvolutionaryAlgorithmWindow import EvolutionaryAlgorithmWindow
from ui.HillClimbWindow import HillClimbWindow
from ui.PSOWindow import PSOWindow


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi("E:/Projects/Lab3/ui/windows/MainWindow.ui", self)

        self.hillClimbButton = self.findChild(QtWidgets.QPushButton, 'buttonHillClimb')
        self.hillClimbButton.clicked.connect(self.hillClimbWindow)

        self.evolutionaryButton = self.findChild(QtWidgets.QPushButton, 'buttonEvolutionary')
        self.evolutionaryButton.clicked.connect(self.evolutionaryWindow)

        self.psoButton = self.findChild(QtWidgets.QPushButton, 'buttonPSO')
        self.psoButton.clicked.connect(self.psoWindow)

        self.show()

    def hillClimbWindow(self):
        self.hillClimbWindow = HillClimbWindow()
        self.hillClimbWindow.show()

    def evolutionaryWindow(self):
        self.evolutionaryWindow = EvolutionaryAlgorithmWindow()
        self.evolutionaryWindow.show()

    def psoWindow(self):
        self.psoWindow = PSOWindow()
        self.psoWindow.show()


def runApp():
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec())


runApp()
