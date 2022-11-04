import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QBrush, QFont, QImage, QPalette, QIcon
from PyQt5.QtCore import QSize


class Widget(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('manual.ui', self)
        oImage = QImage("Pics\\bgframe.png")
        sImage = oImage.scaled(QSize(601, 514))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.pushButton.clicked.connect(self.closeMyApp_OpenNewApp)

    def closeMyApp_OpenNewApp(self):
        self.close()


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())
