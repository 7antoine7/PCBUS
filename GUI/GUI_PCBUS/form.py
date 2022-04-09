# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1378, 864)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Z_down = QPushButton(self.centralwidget)
        self.Z_down.setObjectName(u"Z_down")
        self.Z_down.setGeometry(QRect(430, 240, 90, 150))
        self.Z_down.setMouseTracking(True)
        self.Z_down.setStyleSheet(u"image: url(:/images/assets/down_Z_arrow.png);\n"
"background-color: transparent;")
        self.Z_up = QPushButton(self.centralwidget)
        self.Z_up.setObjectName(u"Z_up")
        self.Z_up.setGeometry(QRect(430, 0, 90, 150))
        self.Z_up.setStyleSheet(u"image: url(:/images/assets/up_Z_arrow.png);\n"
"background-color: transparent;")
        self.X_up = QPushButton(self.centralwidget)
        self.X_up.setObjectName(u"X_up")
        self.X_up.setGeometry(QRect(160, 0, 90, 150))
        self.X_up.setStyleSheet(u"image: url(:/images/assets/up_X_arrow.png);\n"
"background-color: transparent;")
        self.X_down = QPushButton(self.centralwidget)
        self.X_down.setObjectName(u"X_down")
        self.X_down.setGeometry(QRect(160, 240, 90, 150))
        self.X_down.setStyleSheet(u"image: url(:/images/assets/down_X_arrow.png);\n"
"background-color: transparent;")
        self.Y_up = QPushButton(self.centralwidget)
        self.Y_up.setObjectName(u"Y_up")
        self.Y_up.setGeometry(QRect(10, 150, 150, 90))
        self.Y_up.setStyleSheet(u"image: url(:/images/assets/up_Y_arrow.png);\n"
"background-color: transparent;")
        self.Y_down = QPushButton(self.centralwidget)
        self.Y_down.setObjectName(u"Y_down")
        self.Y_down.setGeometry(QRect(250, 150, 150, 90))
        self.Y_down.setStyleSheet(u"image: url(:/images/assets/down_Y_arrow.png);\n"
"background-color: transparent;")
        self.home = QPushButton(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(160, 150, 90, 90))
        self.home.setStyleSheet(u"image: url(:/images/assets/home_button.png);\n"
"border-width: 2px;\n"
"")
        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QRect(590, 560, 90, 90))
        self.play.setStyleSheet(u"image: url(:/images/assets/play_button.png);\n"
"background-color: transparent;")
        self.pause = QPushButton(self.centralwidget)
        self.pause.setObjectName(u"pause")
        self.pause.setGeometry(QRect(740, 560, 90, 90))
        self.pause.setStyleSheet(u"image: url(:/images/assets/pause_button.png);\n"
"background-color: transparent;\n"
"border-color: rgb(0, 0, 0);")
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(890, 560, 90, 90))
        self.stop.setMouseTracking(True)
        self.stop.setFocusPolicy(Qt.ClickFocus)
        self.stop.setStyleSheet(u"image: url(:/images/assets/stop_button.png);\n"
"background-color: transparent;\n"
"border-color: rgb(255, 0, 255);\n"
"border-width: 2px;\n"
"")
        self.IncX = QLabel(self.centralwidget)
        self.IncX.setObjectName(u"IncX")
        self.IncX.setGeometry(QRect(10, 450, 211, 31))
        font = QFont()
        font.setPointSize(24)
        self.IncX.setFont(font)
        self.Incy = QLabel(self.centralwidget)
        self.Incy.setObjectName(u"Incy")
        self.Incy.setGeometry(QRect(10, 500, 211, 31))
        self.Incy.setFont(font)
        self.IncZ = QLabel(self.centralwidget)
        self.IncZ.setObjectName(u"IncZ")
        self.IncZ.setGeometry(QRect(10, 550, 211, 31))
        self.IncZ.setFont(font)
        self.modeManBtn = QPushButton(self.centralwidget)
        self.modeManBtn.setObjectName(u"modeManBtn")
        self.modeManBtn.setGeometry(QRect(590, 460, 135, 76))
        self.modeManBtn.setStyleSheet(u"image: url(:/images/assets/mode_manuel.png);\n"
"")
        self.modeSingleBtn = QPushButton(self.centralwidget)
        self.modeSingleBtn.setObjectName(u"modeSingleBtn")
        self.modeSingleBtn.setGeometry(QRect(730, 460, 135, 76))
        self.modeSingleBtn.setStyleSheet(u"image: url(:/images/assets/mode_cycle.png);\n"
"")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(1160, 610, 201, 31))
        self.progressBar.setValue(24)
        self.machineStatus = QLabel(self.centralwidget)
        self.machineStatus.setObjectName(u"machineStatus")
        self.machineStatus.setGeometry(QRect(590, 0, 291, 71))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setUnderline(True)
        self.machineStatus.setFont(font1)
        self.Speeds = QLabel(self.centralwidget)
        self.Speeds.setObjectName(u"Speeds")
        self.Speeds.setGeometry(QRect(590, 290, 111, 41))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setUnderline(True)
        self.Speeds.setFont(font2)
        self.IncXSld = QSlider(self.centralwidget)
        self.IncXSld.setObjectName(u"IncXSld")
        self.IncXSld.setGeometry(QRect(220, 455, 171, 31))
        self.IncXSld.setMaximum(10)
        self.IncXSld.setOrientation(Qt.Horizontal)
        self.IncXSld.setTickPosition(QSlider.TicksBelow)
        self.IncYSld = QSlider(self.centralwidget)
        self.IncYSld.setObjectName(u"IncYSld")
        self.IncYSld.setGeometry(QRect(220, 505, 171, 31))
        self.IncYSld.setMaximum(10)
        self.IncYSld.setOrientation(Qt.Horizontal)
        self.IncYSld.setTickPosition(QSlider.TicksBelow)
        self.IncZSld = QSlider(self.centralwidget)
        self.IncZSld.setObjectName(u"IncZSld")
        self.IncZSld.setGeometry(QRect(220, 555, 171, 31))
        self.IncZSld.setMaximum(10)
        self.IncZSld.setOrientation(Qt.Horizontal)
        self.IncZSld.setTickPosition(QSlider.TicksBelow)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 440, 16, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 440, 16, 16))
        self.valueIncX = QLabel(self.centralwidget)
        self.valueIncX.setObjectName(u"valueIncX")
        self.valueIncX.setGeometry(QRect(420, 455, 91, 21))
        font3 = QFont()
        font3.setPointSize(14)
        self.valueIncX.setFont(font3)
        self.valueIncY = QLabel(self.centralwidget)
        self.valueIncY.setObjectName(u"valueIncY")
        self.valueIncY.setGeometry(QRect(420, 505, 71, 21))
        self.valueIncY.setFont(font3)
        self.valueIncZ = QLabel(self.centralwidget)
        self.valueIncZ.setObjectName(u"valueIncZ")
        self.valueIncZ.setGeometry(QRect(420, 555, 81, 21))
        self.valueIncZ.setFont(font3)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 490, 16, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 490, 16, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(382, 540, 16, 16))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(220, 540, 16, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 340, 71, 27))
        self.label_3.setFont(font3)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(590, 370, 51, 27))
        self.label_4.setFont(font3)
        self.feedSpeed = QLabel(self.centralwidget)
        self.feedSpeed.setObjectName(u"feedSpeed")
        self.feedSpeed.setGeometry(QRect(730, 370, 82, 27))
        self.feedSpeed.setFont(font3)
        self.spindleSpeed = QLabel(self.centralwidget)
        self.spindleSpeed.setObjectName(u"spindleSpeed")
        self.spindleSpeed.setGeometry(QRect(730, 340, 82, 27))
        self.spindleSpeed.setFont(font3)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(630, 70, 140, 27))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_12.setFont(font4)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(600, 110, 21, 27))
        self.label_14.setFont(font4)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(600, 170, 21, 27))
        self.label_15.setFont(font4)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(600, 230, 21, 27))
        self.label_16.setFont(font4)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(590, 90, 195, 21))
        font5 = QFont()
        font5.setBold(False)
        self.line.setFont(font5)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(590, 145, 195, 20))
        self.line_2.setFont(font5)
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(590, 205, 195, 20))
        self.line_3.setFont(font5)
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(610, 70, 20, 205))
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(775, 70, 20, 205))
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(580, 70, 20, 205))
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(589, 265, 198, 20))
        self.line_8.setFont(font5)
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(589, 60, 195, 20))
        self.line_9.setFont(font5)
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QFrame.HLine)
        self.posX = QLabel(self.centralwidget)
        self.posX.setObjectName(u"posX")
        self.posX.setGeometry(QRect(630, 110, 91, 27))
        font6 = QFont()
        font6.setPointSize(16)
        self.posX.setFont(font6)
        self.posY = QLabel(self.centralwidget)
        self.posY.setObjectName(u"posY")
        self.posY.setGeometry(QRect(630, 170, 101, 27))
        self.posY.setFont(font6)
        self.posZ = QLabel(self.centralwidget)
        self.posZ.setObjectName(u"posZ")
        self.posZ.setGeometry(QRect(630, 230, 111, 27))
        self.posZ.setFont(font6)
        self.comportCombo = QComboBox(self.centralwidget)
        self.comportCombo.setObjectName(u"comportCombo")
        self.comportCombo.setGeometry(QRect(1070, 580, 121, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1070, 520, 201, 24))
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(1280, 520, 80, 24))
        self.modeLabel = QLabel(self.centralwidget)
        self.modeLabel.setObjectName(u"modeLabel")
        self.modeLabel.setGeometry(QRect(590, 410, 451, 41))
        self.modeLabel.setFont(font)
        self.gcodeView = QTextEdit(self.centralwidget)
        self.gcodeView.setObjectName(u"gcodeView")
        self.gcodeView.setGeometry(QRect(1070, 20, 291, 491))
        self.refreshBtn = QPushButton(self.centralwidget)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setGeometry(QRect(1260, 550, 80, 24))
        self.connectBtn = QPushButton(self.centralwidget)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setGeometry(QRect(1070, 550, 80, 24))
        self.disconnectBtn = QPushButton(self.centralwidget)
        self.disconnectBtn.setObjectName(u"disconnectBtn")
        self.disconnectBtn.setGeometry(QRect(1160, 550, 90, 24))
        self.openFile = QPushButton(self.centralwidget)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setGeometry(QRect(1070, 610, 81, 31))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(370, 645, 41, 20))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(220, 645, 16, 16))
        self.IncSpeedSld = QSlider(self.centralwidget)
        self.IncSpeedSld.setObjectName(u"IncSpeedSld")
        self.IncSpeedSld.setGeometry(QRect(220, 660, 171, 31))
        self.IncSpeedSld.setMaximum(18000)
        self.IncSpeedSld.setPageStep(1000)
        self.IncSpeedSld.setOrientation(Qt.Horizontal)
        self.IncSpeedSld.setTickPosition(QSlider.TicksBelow)
        self.Incy_2 = QLabel(self.centralwidget)
        self.Incy_2.setObjectName(u"Incy_2")
        self.Incy_2.setGeometry(QRect(10, 605, 211, 31))
        self.Incy_2.setFont(font)
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(220, 595, 16, 16))
        self.valueIncSpeed = QLabel(self.centralwidget)
        self.valueIncSpeed.setObjectName(u"valueIncSpeed")
        self.valueIncSpeed.setGeometry(QRect(420, 660, 131, 21))
        self.valueIncSpeed.setFont(font3)
        self.IncZ_2 = QLabel(self.centralwidget)
        self.IncZ_2.setObjectName(u"IncZ_2")
        self.IncZ_2.setGeometry(QRect(10, 640, 211, 51))
        self.IncZ_2.setFont(font)
        self.valueIncFeed = QLabel(self.centralwidget)
        self.valueIncFeed.setObjectName(u"valueIncFeed")
        self.valueIncFeed.setGeometry(QRect(420, 610, 121, 21))
        self.valueIncFeed.setFont(font3)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(375, 595, 21, 20))
        self.IncFeedSld = QSlider(self.centralwidget)
        self.IncFeedSld.setObjectName(u"IncFeedSld")
        self.IncFeedSld.setGeometry(QRect(220, 610, 171, 31))
        self.IncFeedSld.setMaximum(900)
        self.IncFeedSld.setPageStep(50)
        self.IncFeedSld.setOrientation(Qt.Horizontal)
        self.IncFeedSld.setTickPosition(QSlider.TicksBelow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1378, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh Ports S\u00e9ries", None))
        self.Z_down.setText("")
        self.Z_up.setText("")
        self.X_up.setText("")
        self.X_down.setText("")
        self.Y_up.setText("")
        self.Y_down.setText("")
        self.home.setText("")
        self.play.setText("")
        self.pause.setText("")
        self.stop.setText("")
        self.IncX.setText(QCoreApplication.translate("MainWindow", u"Incr\u00e9ments X :", None))
        self.Incy.setText(QCoreApplication.translate("MainWindow", u"Incr\u00e9ments Y :", None))
        self.IncZ.setText(QCoreApplication.translate("MainWindow", u"Incr\u00e9ments Z :", None))
        self.modeManBtn.setText("")
        self.modeSingleBtn.setText("")
        self.machineStatus.setText(QCoreApplication.translate("MainWindow", u"Machine Status", None))
        self.Speeds.setText(QCoreApplication.translate("MainWindow", u"Speeds", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.valueIncX.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.valueIncY.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.valueIncZ.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Spindle : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Feed : ", None))
        self.feedSpeed.setText(QCoreApplication.translate("MainWindow", u"0 mm/s", None))
        self.spindleSpeed.setText(QCoreApplication.translate("MainWindow", u"0 rpm", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Position (mm)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.posX.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.posY.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.posZ.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.modeLabel.setText(QCoreApplication.translate("MainWindow", u"Mode Actuel : ", None))
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnectBtn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.openFile.setText(QCoreApplication.translate("MainWindow", u"Ouvrir Fichier", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"18000", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Incy_2.setText(QCoreApplication.translate("MainWindow", u"Feed :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.valueIncSpeed.setText(QCoreApplication.translate("MainWindow", u"0 rpm", None))
        self.IncZ_2.setText(QCoreApplication.translate("MainWindow", u"Speed :", None))
        self.valueIncFeed.setText(QCoreApplication.translate("MainWindow", u"0 mm/min", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"900", None))
    # retranslateUi

