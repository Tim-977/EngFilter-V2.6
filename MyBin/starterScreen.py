import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('loading.ui', self)
        self.progressBar.setValue(0)
    



if True:
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
