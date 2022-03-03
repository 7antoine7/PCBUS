import sys

from PySide6 import QtGui, QtWidgets

from form import Ui_MainWindow
import resources


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Super PCBUS CNC MASTER CONFIGURATOR 9000")

        self.gcodeView.setReadOnly(True)

        #Assignation des bouttons aux fonctions
        self.X_up.clicked.connect(self.moveXUp)
        self.X_down.clicked.connect(self.moveXDown)
        self.Y_up.clicked.connect(self.moveYUp)
        self.Y_down.clicked.connect(self.moveYDown)
        self.Z_up.clicked.connect(self.moveZUp)
        self.Z_down.clicked.connect(self.moveZDown)

    def moveXUp(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = "10"
        self.sendCommand("G1 X" + distance)

    def moveXDown(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = "-10"
        self.sendCommand("G1 X" + distance)

    def moveYUp(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = "10"
        self.sendCommand("G1 Y" + distance)

    def moveYDown(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = "-10"
        self.sendCommand("G1 Y" + distance)

    def moveZUp(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = "10"
        self.sendCommand("G1 Z" + distance)

    def moveZDown(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = "-10"
        self.sendCommand("G1 Z" + distance)

    def sendCommand(self, command):
        self.gcodeView.appendPlainText(command)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()


window.show()
app.exec_()
