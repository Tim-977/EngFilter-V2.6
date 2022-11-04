from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QBrush, QImage, QPalette
from PyQt5.QtWidgets import QWidget

import dbparser as dbp


class Final(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('final.ui', self)
        oImage = QImage("Pics\\bgframe.png")
        sImage = oImage.scaled(QSize(611, 524))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.pushButton.clicked.connect(self.sendReview)

    def sendReview(self):
        mark = self.horizontalSlider.value()
        comment = self.plainTextEdit.toPlainText()
        dbp.insert_result('reviews.db', mark, comment)
        self.close()


ex = Final()
ex.show()
