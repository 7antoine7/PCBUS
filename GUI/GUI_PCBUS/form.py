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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1378, 864)
        self.actionConnection = QAction(MainWindow)
        self.actionConnection.setObjectName(u"actionConnection")
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
        self.mesh = QPushButton(self.centralwidget)
        self.mesh.setObjectName(u"mesh")
        self.mesh.setGeometry(QRect(430, 150, 90, 90))
        self.mesh.setStyleSheet(u"image: url(:/images/assets/mesh_button.png);\n"
"background-color: transparent;\n"
"")
        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QRect(30, 710, 90, 90))
        self.play.setStyleSheet(u"image: url(:/images/assets/play_button.png);\n"
"background-color: transparent;")
        self.pause = QPushButton(self.centralwidget)
        self.pause.setObjectName(u"pause")
        self.pause.setGeometry(QRect(180, 710, 90, 90))
        self.pause.setStyleSheet(u"image: url(:/images/assets/pause_button.png);\n"
"background-color: transparent;\n"
"border-color: rgb(0, 0, 0);")
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(330, 710, 90, 90))
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
        self.IncX_choix = QToolButton(self.centralwidget)
        self.IncX_choix.setObjectName(u"IncX_choix")
        self.IncX_choix.setGeometry(QRect(220, 455, 71, 31))
        self.IncZ_choix = QToolButton(self.centralwidget)
        self.IncZ_choix.setObjectName(u"IncZ_choix")
        self.IncZ_choix.setGeometry(QRect(220, 555, 71, 31))
        self.IncY_choix = QToolButton(self.centralwidget)
        self.IncY_choix.setObjectName(u"IncY_choix")
        self.IncY_choix.setGeometry(QRect(220, 505, 71, 31))
        self.Mode_man = QPushButton(self.centralwidget)
        self.Mode_man.setObjectName(u"Mode_man")
        self.Mode_man.setGeometry(QRect(160, 620, 135, 76))
        self.Mode_man.setStyleSheet(u"image: url(:/images/assets/mode_manuel.png);\n"
"")
        self.Mode_auto = QPushButton(self.centralwidget)
        self.Mode_auto.setObjectName(u"Mode_auto")
        self.Mode_auto.setGeometry(QRect(10, 620, 135, 76))
        self.Mode_auto.setStyleSheet(u"image: url(:/images/assets/mode_auto.png);\n"
"")
        self.Mode_single = QPushButton(self.centralwidget)
        self.Mode_single.setObjectName(u"Mode_single")
        self.Mode_single.setGeometry(QRect(310, 620, 135, 76))
        self.Mode_single.setStyleSheet(u"image: url(:/images/assets/mode_cycle.png);\n"
"")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(580, 710, 250, 45))
        self.progressBar.setValue(24)
        self.machine_Status = QLabel(self.centralwidget)
        self.machine_Status.setObjectName(u"machine_Status")
        self.machine_Status.setGeometry(QRect(620, 0, 291, 71))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setUnderline(True)
        self.machine_Status.setFont(font1)
        self.table_Status = QTableView(self.centralwidget)
        self.table_Status.setObjectName(u"table_Status")
        self.table_Status.setGeometry(QRect(590, 70, 256, 192))
        self.table_speeds = QTableView(self.centralwidget)
        self.table_speeds.setObjectName(u"table_speeds")
        self.table_speeds.setGeometry(QRect(590, 380, 256, 192))
        self.Speeds = QLabel(self.centralwidget)
        self.Speeds.setObjectName(u"Speeds")
        self.Speeds.setGeometry(QRect(590, 330, 111, 41))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setUnderline(True)
        self.Speeds.setFont(font2)
        self.OpenFile = QPushButton(self.centralwidget)
        self.OpenFile.setObjectName(u"OpenFile")
        self.OpenFile.setGeometry(QRect(580, 610, 150, 90))
        self.OpenFile.setStyleSheet(u"image: url(:/assets/ouvrir_fichier_boutton.png);")
        self.e_Stop = QPushButton(self.centralwidget)
        self.e_Stop.setObjectName(u"e_Stop")
        self.e_Stop.setGeometry(QRect(1170, 640, 181, 181))
        self.e_Stop.setStyleSheet(u"image: url(:/images/assets/e-stop.png);")
        self.gcodeView = QPlainTextEdit(self.centralwidget)
        self.gcodeView.setObjectName(u"gcodeView")
        self.gcodeView.setGeometry(QRect(1080, 0, 281, 511))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1378, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionConnection)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnection.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.Z_down.setText("")
        self.Z_up.setText("")
        self.X_up.setText("")
        self.X_down.setText("")
        self.Y_up.setText("")
        self.Y_down.setText("")
        self.home.setText("")
        self.mesh.setText("")
        self.play.setText("")
        self.pause.setText("")
        self.stop.setText("")
        self.IncX.setText(QCoreApplication.translate("MainWindow", u"Incr\u00e9ments X :", None))
        self.Incy.setText(QCoreApplication.translate("MainWindow", u"Incr\u00e9ments Y :", None))
        self.IncZ.setText(QCoreApplication.translate("MainWindow", u"Incr\u00e9ments Z :", None))
        self.IncX_choix.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.IncZ_choix.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.IncY_choix.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Mode_man.setText("")
        self.Mode_auto.setText("")
        self.Mode_single.setText("")
        self.machine_Status.setText(QCoreApplication.translate("MainWindow", u"Machine Status", None))
        self.Speeds.setText(QCoreApplication.translate("MainWindow", u"Speeds", None))
        self.OpenFile.setText("")
        self.e_Stop.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

