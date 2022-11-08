import sys

from deep_translator import GoogleTranslator
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

print('SCAN STARTED')


class MyError(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('error.ui', self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.pushButton.clicked.connect(self.alert)

    def alert(self): # Функция, которая вызывается в случае отсутствия текса
        try:
            raise SystemError
        except:
            sys.exit()


class MyWidget1(QMainWindow): # Класс, поддерживающий окно загрузки

    def __init__(self):
        super().__init__()
        uic.loadUi('loading.ui', self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setFixedWidth(405)
        self.setFixedHeight(189)
        self.progressBar.setValue(0)
        self.f = open('text.txt')
        self.out = open('res.txt', 'w')
        self.out2 = open('word_list.txt', 'w')
        self.out_tr = open('translated_list.txt', 'w', encoding='utf-8')
        self.st = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        self.st2 = '"?!/.,:;()*@~`{[}]<>_-—+= '
        self.words = set([])
        self.word = ''
        self.entireText = self.f.readlines()
        self.pushButton.clicked.connect(self.main)
        self.label_file.setText('')

    def tran(self, to_translate):  # Функция перевода слов
        return GoogleTranslator(source='en',
                                target='ru').translate(to_translate)

    def main(self):  # Функция, запускающая алгоритм сортировки слов
        self.pushButton.hide()
        # Цикл, разделяющий текст на слова
        for self.i in self.entireText:
            for self.j in self.i + ' ':
                if self.j in self.st2:
                    if self.word != ' ' and self.word != '':
                        self.words.add(self.word.lower())
                        self.word = ''
                else:
                    if self.j in self.st:
                        self.word += self.j

        # Сортировка слов и удаления дубликатов

        self.words = list(self.words)
        self.words.sort()
        print(self.words)
        self.i = 0

        self.x = len(self.words)

        if not self.x:  # Проверка на наличие слов
            print('ERROR: YOU DONT HAVE ANY TEXT')
            self.w = MyError()
            self.w.show()
        # Алгоритм, удаляющий схожие формы слов
        while self.i < len(self.words) - 1:
            if self.words[self.i] + 's' == self.words[
                    self.i +
                    1] or self.words[self.i] + 'es' == self.words[self.i + 1]:
                self.words.pop(self.i + 1)
                self.i -= 2

            if self.words[self.i] + 'd' == self.words[
                    self.i +
                    1] or self.words[self.i] + 'ed' == self.words[self.i + 1]:
                self.words.pop(self.i + 1)
                self.i -= 2

            if self.words[self.i] + 'ing' == self.words[self.i + 1]:
                self.words.pop(self.i + 1)
                self.i -= 2

            if self.words[self.i] + 'er' == self.words[self.i + 1]:
                self.words.pop(self.i + 1)
                self.i -= 2

            if self.words[self.i] + 'ly' == self.words[self.i + 1]:
                self.words.pop(self.i + 1)
                self.i -= 2

            self.i += 1

        self.x = 0

        # Наполнение файлом готовыми словами и их переводами

        for self.i in self.words:
            self.x += 1
            print(f"{self.x * 100 // len(self.words)}% | {self.x} | {self.i}")
            self.label_file.setText(self.i)
            self.progressBar.setValue((self.x) * 100 // len(self.words))
            self.out.writelines(self.i + '\n')
            self.out2.writelines(self.i + '\n')
            self.out_tr.writelines(self.tran(self.i) + '\n')
        self.label_file.setText('Process completed successfully')
        print(self.words)

        # Закрытие файлов

        self.f.close()
        self.out.close()
        self.out2.close()
        self.out_tr.close()
        self.close()


app = QApplication(sys.argv)
ex = MyWidget1()
ex.show()
app.exec_()
