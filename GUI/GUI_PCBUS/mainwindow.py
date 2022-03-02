import sys

from PySide6 import QtGui, QtWidgets

from form import Ui_MainWindow
import resources


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Super PCBUS CNC MASTER CONFIGURATOR 9000")
        self.pushButton.clicked.connect(self.change_text)

    def change_text(self):
        self.pushButton.setText("fuck you")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()


window.show()
app.exec_()
