from cgitb import text
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
        self.currentState = None

        self.gcodeView.setReadOnly(True)
    
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

        self.play.clicked.connect(self.sendCommandSingle)

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
            distance = str(self.IncXSld.value() + float(self.posX.text()))
            feed = str(self.IncFeedSld.value())
            self.sendCommand("G1 X" + distance + " F" + feed)
        pass

    def moveXDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1*self.IncXSld.value() + float(self.posX.text()))
            feed = str(self.IncFeedSld.value())
            self.sendCommand("G1 X" + distance + " F" + feed)
        pass

    def moveYUp(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(self.IncYSld.value() + float(self.posY.text()))
            feed = str(self.IncFeedSld.value())
            self.sendCommand("G1 Y" + distance + " F" + feed)
        pass

    def moveYDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1*self.IncYSld.value() + float(self.posY.text()))
            feed = str(self.IncFeedSld.value())
            self.sendCommand("G1 Y" + distance + " F" + feed)
        pass

    def moveZUp(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(1/10*self.IncZSld.value() + float(self.posZ.text()))
            feed = str(self.IncFeedSld.value())
            self.sendCommand("G1 Z" + distance + " F" + feed)
        pass

    def moveZDown(self):
        if self.currentMode == "Manuel":
            # La distance viendrait des sliders pour choisir les increments
            distance = str(-1/10*self.IncZSld.value() + float(self.posZ.text()))
            feed = str(self.IncFeedSld.value())
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

    def sendCommandSingle(self):
        if self.currentMode == "Single":
            if self.currentState == "Idle":
                self.sendCommand(self.commandesFichier.pop())
            

    def updatePorts(self):
        self.comportCombo.addItems(self.serial.listPort())

    def changePort(self):
        self.serial.setPort(self.comportCombo.currentText())

    def sendSerial(self):
        text = self.lineEdit.text()
        self.sendCommand(text)

    def updateSerial(self):
        self.serial.send("?")
        lines = self.serial.update()
        if lines is not None:
            self.gcodeView.setTextColor(QtGui.QColor('#4040AD'))
            for line in lines:
                match = re.match(
                    r"<(?P<State>Idle|Run|Hold|Home|Alarm|Check|Door)(?:\|MPos:(?P<MX>-?[0-9\.]*),(?P<MY>-?[0-9\.]*),(?P<MZ>-?[0-9\.]*))?(?:\|WPos:(?P<WX>-?[0-9\.]*),(?P<WY>-?[0-9\.]*),(?P<WZ>-?[0-9\.]*))?(?:\|FS:(?P<F>[0-9\.]*),(?P<S>[0-9\.]*))?(?:\|WCO:(?P<WcoX>[0-9\.]*),(?P<WcoY>[0-9\.]*),(?P<WcoZ>[0-9\.]*))?(?:\|Buf:(?P<Buf>[0-9]*))?(?:\|RX:(?P<RX>[0-9]*))?(?:\|Ln:(?P<L>[0-9]*))?(?:\|Lim:(?P<Lim>[0-1]*))?(?:\|Ctl:(?:'Ctl'[0-1]*))?(?:\|Ov:(?P<OvX>[0-9\.]*),(?P<OvY>[0-9\.]*),(?P<OvZ>[0-9\.]*))?>", line, re.S)
                if match:
                    dict = match.groupdict()
                    self.currentState = dict["State"]
                    self.posX.setText(dict["MX"])
                    self.posY.setText(dict["MY"])
                    self.posZ.setText(dict["MZ"])
                    self.spindleSpeed.setText(dict["S"] + " rpm")
                    self.feedSpeed.setText(dict["F"] + " mm/min")
                elif line == "ok":
                    pass
                else:
                    self.gcodeView.append(str(line))


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec_()
