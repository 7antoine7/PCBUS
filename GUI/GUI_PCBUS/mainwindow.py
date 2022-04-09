import sys
from turtle import color

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import *

from form import Ui_MainWindow
import resources
import re
import serialCommunication


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Super PCBUS CNC MASTER CONFIGURATOR 9000")

        self.commandesFichier = []
        self.currentMode = None

        self.gcodeView.setReadOnly(True)

        # Il faudrait trouver une meilleure facon, car pour l'instant le Z
        # va de 0 a 10 et puis je ne sais pas comment mettre les unites.
        self.IncXSld.valueChanged.connect(self.updateIncValues)
        self.IncYSld.valueChanged.connect(self.updateIncValues)
        self.IncZSld.valueChanged.connect(self.updateIncValues)
        self.IncFeedSld.valueChanged.connect(self.updateIncValues)
        self.IncSpeedSld.valueChanged.connect(self.updateIncValues)

        # Assignation des bouttons aux fonctions
        self.X_up.clicked.connect(self.moveXUp)
        self.X_down.clicked.connect(self.moveXDown)
        self.Y_up.clicked.connect(self.moveYUp)
        self.Y_down.clicked.connect(self.moveYDown)
        self.Z_up.clicked.connect(self.moveZUp)
        self.Z_down.clicked.connect(self.moveZDown)
        self.home.clicked.connect(self.homeXY)
        self.openFile.clicked.connect(self.readFile)

        self.modeManBtn.clicked.connect(self.modeManuel)
        self.modeSingleBtn.clicked.connect(self.modeSingle)

        self.serial = serialCommunication.serialCommunication()
        self.refreshBtn.clicked.connect(self.updatePorts)
        self.comportCombo.activated.connect(self.changePort)
        self.connectBtn.clicked.connect(self.serial.connect)
        self.disconnectBtn.clicked.connect(self.serial.disconnect)
        self.sendButton.clicked.connect(self.sendSerial)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateSerial)
        self.timer.start(100)  # every 10,000 milliseconds
        self.updatePorts()

    def updateIncValues(self):
        self.valueIncX.setText(str(self.IncXSld.value()) + " mm")
        self.valueIncY.setText(str(self.IncYSld.value()) + " mm")
        self.valueIncZ.setText(str(self.IncZSld.value()/10) + " mm")
        self.valueIncFeed.setText(str(self.IncFeedSld.value()) + " mm/min")
        self.valueIncSpeed.setText(str(self.IncSpeedSld.value()) + " rpm")

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
            feed = str(self.IncFeedSlde.value())
            self.sendCommand("G1 X" + distance + " F" + feed)
        pass

    def moveXDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1*self.IncXSld.value())
            feed = str(self.IncFeedSlde.value())
            self.sendCommand("G1 X" + distance + " F" + feed)
        pass

    def moveYUp(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(self.IncYSld.value())
            feed = str(self.IncFeedSlde.value())
            self.sendCommand("G1 Y" + distance + " F" + feed)
        pass

    def moveYDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1*self.IncYSld.value())
            feed = str(self.IncFeedSlde.value())
            self.sendCommand("G1 Y" + distance + " F" + feed)
        pass

    def moveZUp(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(1*self.IncZSld.value())
            feed = str(self.IncFeedSlde.value())
            self.sendCommand("G1 Z" + distance + " F" + feed)
        pass

    def moveZDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1*self.IncZSld.value())
            feed = str(self.IncFeedSlde.value())
            self.sendCommand("G1 Z" + distance + " F" + feed)
        pass

    def homeXY(self):
        self.sendCommand("G28 X0 Y0")

    def readFile(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]

        file = open(str(path))
        self.commandesFichier = file.readlines()

    def sendCommand(self, command):
        self.gcodeView.setTextColor(QtGui.QColor('#C33332'))
        self.gcodeView.append(command)
        self.serial.send(command)

    def updatePorts(self):
        self.comportCombo.addItems(self.serial.listPort())

    def changePort(self):
        self.serial.setPort(self.comportCombo.currentText())

    def sendSerial(self):
        text = self.lineEdit.text()
        self.sendCommand(text)

    def updateSerial(self):
        lines = self.serial.update()
        if lines is not None:
            self.gcodeView.setTextColor(QtGui.QColor('#4040AD'))
            for line in lines:
                match = re.match(
                    "/<(?'State'Idle|Run|Hold|Home|Alarm|Check|Door)(?:\|MPos:(?'MX'[0-9\.]*),(?'MY'[0-9\.]*),(?'MZ'[0-9\.]*))?(?:\|FS:(?'FEED'[0-9\.]*),(?'SPEED'[0-9\.]*))?>/g", line, re.S)
                if match:
                    dict = match.groupdict()
                    self.posX.setText(dict["MX"])
                    self.posY.setText(dict["MY"])
                    self.posZ.setText(dict["MZ"])

                else:
                    self.gcodeView.append(str(line))


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec_()
