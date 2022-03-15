import sys

from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import *

from form import Ui_MainWindow
import resources

import serial
import serial.tools.list_ports


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Super PCBUS CNC MASTER CONFIGURATOR 9000")

        self.commandesFichier = []

        self.gcodeView.setReadOnly(True)

      # self.creatingTableStatus()

        #Il faudrait trouver une meilleure facon, car pour l'instant le Z
        #va de 0 a 10 et puis je ne sais pas comment mettre les unites.
        self.IncXSld.valueChanged.connect(self.valueIncX.setNum)
        self.IncYSld.valueChanged.connect(self.valueIncY.setNum)
        self.IncZSld.valueChanged.connect(self.valueIncZ.setNum)

        #Assignation des bouttons aux fonctions
        self.X_up.clicked.connect(self.moveXUp)
        self.X_down.clicked.connect(self.moveXDown)
        self.Y_up.clicked.connect(self.moveYUp)
        self.Y_down.clicked.connect(self.moveYDown)
        self.Z_up.clicked.connect(self.moveZUp)
        self.Z_down.clicked.connect(self.moveZDown)
        self.home.clicked.connect(self.homeXY)
        self.mesh.clicked.connect(self.meshZ)
        self.openFile.clicked.connect(self.readFile)

        self.actionRefresh.triggered.connect(self.updatePorts)


    #pt pas la meilleure solution, modifiable quand la fenetre run.
    def creatingTableStatus(self):
        self.tableStatus.setRowCount(4)
        self.tableStatus.setColumnCount(3)

        self.tableStatus.setItem(0, 1, QTableWidgetItem("Position"))
        self.tableStatus.setItem(0, 2, QTableWidgetItem("Distance to Go"))
        self.tableStatus.setItem(1, 0, QTableWidgetItem("X"))
        self.tableStatus.setItem(2, 0, QTableWidgetItem("Y"))
        self.tableStatus.setItem(3, 0, QTableWidgetItem("Z"))

        self.tableStatus.showGrid()

    def moveXUp(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = str(self.IncXSld.value())
        self.sendCommand("G1 X" + distance)

    def moveXDown(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = str(-1*self.IncXSld.value())
        self.sendCommand("G1 X" + distance)

    def moveYUp(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = str(self.IncYSld.value())
        self.sendCommand("G1 Y" + distance)

    def moveYDown(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = str(-1*self.IncYSld.value())
        self.sendCommand("G1 Y" + distance)

    def moveZUp(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = str(1*self.IncZSld.value())
        self.sendCommand("G1 Z" + distance)

    def moveZDown(self):
        #La distance viendrait des toolButton pour choisir les increments
        distance = str(-1*self.IncZSld.value())
        self.sendCommand("G1 Z" + distance)

    def homeXY(self):
        self.sendCommand("G28 X0 Y0")

    def meshZ(self):
        self.sendCommand("G30")

    def readFile(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        file = open(str(path))
        self.commandesFichier = file.readlines()

    def sendCommand(self, command):
        self.gcodeView.appendPlainText(command)

    def updatePorts(self):
        pass




app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec_()
