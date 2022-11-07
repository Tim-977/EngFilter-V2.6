from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

import dbparser as dbp  # Подключение модуля для работы с БД


class Final(QWidget):  # Класс, поддерживающий окно обратной связи

    def __init__(self):
        super().__init__()
        uic.loadUi('final.ui', self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setFixedWidth(619)
        self.setFixedHeight(538)
        self.pushButton.clicked.connect(self.sendReview)

    def sendReview(self):  # Вставление данных в БД
        mark = self.horizontalSlider.value()
        comment = self.plainTextEdit.toPlainText()
        dbp.insert_result('reviews.db', mark, comment)
        self.close()


ex = Final()
ex.show()
