import sys

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import *

from form import Ui_MainWindow
import resources

import serialCommunication


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Super PCBUS CNC MASTER CONFIGURATOR 9000")

        self.commandesFichier = []
        self.currentMode = None

        self.gcodeView.setReadOnly(True)

      # self.creatingTableStatus()

        # Il faudrait trouver une meilleure facon, car pour l'instant le Z
        # va de 0 a 10 et puis je ne sais pas comment mettre les unites.
        self.IncXSld.valueChanged.connect(self.valueIncX.setNum)
        self.IncYSld.valueChanged.connect(self.valueIncY.setNum)
        self.IncZSld.valueChanged.connect(self.valueIncZ.setNum)

        # Assignation des bouttons aux fonctions
        self.X_up.clicked.connect(self.moveXUp)
        self.X_down.clicked.connect(self.moveXDown)
        self.Y_up.clicked.connect(self.moveYUp)
        self.Y_down.clicked.connect(self.moveYDown)
        self.Z_up.clicked.connect(self.moveZUp)
        self.Z_down.clicked.connect(self.moveZDown)
        self.home.clicked.connect(self.homeXY)
        self.mesh.clicked.connect(self.meshZ)
        self.openFile.clicked.connect(self.readFile)

        self.modeAutoBtn.clicked.connect(self.modeAuto)
        self.modeManBtn.clicked.connect(self.modeManuel)
        self.modeSingleBtn.clicked.connect(self.modeSingle)

        self.serial = serialCommunication.serialCommunication()
        self.actionRefresh.triggered.connect(self.updatePorts)
        self.comportCombo.activated.connect(self.changePort)
        self.actionConnect.triggered.connect(self.serial.connect)
        self.actionDisconnect.triggered.connect(self.serial.disconnect)
        self.sendButton.clicked.connect(self.sendSerial)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.serial.update)
        self.timer.start(100)  # every 10,000 milliseconds

    def modeAuto(self):
        self.modeLabel.setText("Mode Actuel : AUTO")
        self.currentMode = "Auto"
        pass

    def modeManuel(self):
        self.modeLabel.setText("Mode Actuel : MANUEL")
        self.currentMode = "Manuel"
        pass

    def modeSingle(self):
        self.modeLabel.setText("Mode Actuel : SINGLE BLOCK")
        self.currentMode = "Single"
        pass

    def moveXUp(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(self.IncXSld.value())
            self.sendCommand("G1 X" + distance)
        pass

    def moveXDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1*self.IncXSld.value())
            self.sendCommand("G1 X" + distance)
        pass

    def moveYUp(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(self.IncYSld.value())
            self.sendCommand("G1 Y" + distance)
        pass

    def moveYDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1*self.IncYSld.value())
            self.sendCommand("G1 Y" + distance)
        pass

    def moveZUp(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(1*self.IncZSld.value())
            self.sendCommand("G1 Z" + distance)
        pass

    def moveZDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1*self.IncZSld.value())
            self.sendCommand("G1 Z" + distance)
        pass

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
        self.serial.send(command)

    def updatePorts(self):
        self.comportCombo.addItems(self.serial.listPort())

    def changePort(self):
        self.serial.setPort(self.comportCombo.currentText())

    def sendSerial(self):
        text = self.lineEdit.text() + "\n"
        self.sendCommand(text)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec_()
