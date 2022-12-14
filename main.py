import sys

from deep_translator import GoogleTranslator
from PyQt5 import QtCore, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

import first_scan  # Запускаю модуль обработки изначального текста и разделения слов

# Открытие необходимых файлов и создание стурктур данных

f = open('word_list.txt')
outnew = open('new.txt', 'w', encoding='utf-8')
outold = open('notnew.txt', 'w')
translated = open('translated_list.txt', 'r', encoding='utf-8')

st = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
st2 = '"?!/.,:;()*@~`{[}]<>_-—+= '
words = set([])
word = ''
i = ''

# Цикл, делающий множество слов и удаляющий повторения

for i in f.readlines():
    for j in i + ' ':
        if j in st2:
            if word != ' ' and word != '':
                words.add(word.lower())
                print(f"w: {words}")
                word = ''
        else:
            if j in st:
                word += j

# Делаем из множества список и сортируем его

words = list(words)
words.sort()
print(f"WORDS: {words}")

if not len(words):  # Проверка на наличие слов
    print('ERROR: YOU DONT HAVE ANY TEXT')
    sys.exit()


class Window2(QWidget):  # Класс, создающий окно инструкции

    def __init__(self):
        super().__init__()
        uic.loadUi('manual.ui', self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setFixedWidth(627)
        self.setFixedHeight(671)
        self.pushButton.clicked.connect(self.closeMyApp_OpenNewApp)
        self.eggBtn.clicked.connect(self.easterEgg)

    def closeMyApp_OpenNewApp(self):
        self.close()

    def easterEgg(self):
        self.setFixedWidth(840)
        self.setFixedHeight(867)


class MyWidget(QMainWindow):  # Класс, создающий главное окно

    def __init__(self):
        super().__init__()
        uic.loadUi('EngFilUi.ui', self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setFixedWidth(903)
        self.setFixedHeight(731)
        self.flag = []
        self.words = words
        self.b = 0
        self.x = 0
        self.newWords = []
        self.oldWords = []
        self.translatedWords = translated.readlines()
        self.i = words[self.x]
        self.lel = len(self.words)
        self.left_numLbl.setText(str(len(self.words)))
        self.originalLabel.setText(self.i)
        self.translatedLabel.setText(self.translatedWords[self.x])
        self.word_3.setText('')
        self.word_2.setText('')
        self.word_1.setText('')
        self.word0.setText(self.i)
        if self.x >= len(self.words) - 1:
            self.word1.setText('')
        else:
            self.word1.setText(self.words[self.x + 1])
        if self.x >= len(self.words) - 2:
            self.word2.setText('')
        else:
            self.word2.setText(self.words[self.x + 2])
        if self.x >= len(self.words) - 3:
            self.word3.setText('')
        else:
            self.word3.setText(self.words[self.x + 3])

        self.newBtn.clicked.connect(self.byes)
        self.oldBtn.clicked.connect(self.bno)
        self.manualBtn.clicked.connect(self.window2)
        self.stepBtn.setEnabled(False)
        self.stepBtn.clicked.connect(self.stepback)

    def keyPressEvent(self, event):  # Подключение горячих клавиш
        if event.key() == Qt.Key_D and len(self.words) - self.b != 0:
            self.byes()
        if event.key() == Qt.Key_A and len(self.words) - self.b != 0:
            self.bno()
        if event.key() == Qt.Key_Z and len(
                self.flag) > 0 and len(self.words) - self.b != 0:
            self.stepback()
        if event.key() == Qt.Key_F1 and len(self.words) - self.b != 0:
            self.window2()

    def window2(self):  # Вызов окна с инструкцией
        self.w = Window2()
        self.w.show()

    def tran(self, to_translate):  # Функция перевода
        return GoogleTranslator(source='en',
                                target='ru').translate(to_translate)

    def stepback(self):  # Кнопка Шаг Назад
        if len(self.flag) == 1:
            self.stepBtn.setEnabled(False)
        self.x -= 1
        self.b -= 1
        self.i = self.words[self.x]
        self.left_numLbl.setText(str(len(self.words) - self.b))
        self.behind_numLbl.setText(str(self.b))
        # Форматтер шрифта на случай длинного слова
        if len(self.words[self.x]) > 15:
            self.originalLabel.setFont(QFont('Tempus Sans ITC', 30))
        else:
            self.originalLabel.setFont(QFont('Tempus Sans ITC', 36))
        self.originalLabel.setText(self.words[self.x])
        if len(self.translatedWords[self.x]) > 12:
            self.translatedLabel.setFont(QFont('Tempus Sans ITC', 28))
        else:
            self.translatedLabel.setFont(QFont('Tempus Sans ITC', 36))
        self.translatedLabel.setText(self.translatedWords[self.x])
        self.progressBar.setValue((self.x) * 100 // len(self.words))
        # Смена слов в столбике посередине
        if self.x < 3:
            self.word_3.setText('')
        else:
            self.word_3.setText(self.words[self.x - 3])
        if self.x < 2:
            self.word_2.setText('')
        else:
            self.word_2.setText(self.words[self.x - 2])
        if self.x < 1:
            self.word_1.setText('')
        else:
            self.word_1.setText(self.words[self.x - 1])

        self.word0.setText(self.i)

        if self.x >= len(self.words) - 1:
            self.word1.setText('')
        else:
            self.word1.setText(self.words[self.x + 1])
        if self.x >= len(self.words) - 2:
            self.word2.setText('')
        else:
            self.word2.setText(self.words[self.x + 2])
        if self.x >= len(self.words) - 3:
            self.word3.setText('')
        else:
            self.word3.setText(self.words[self.x + 3])
        if self.flag[-1] == 'yes':
            self.newWords.pop()
            self.flag.pop()
        elif self.flag[-1] == 'no':
            self.oldWords.pop()
            self.flag.pop()
        print('Stepped back')
        print(f'New: {self.newWords}')
        print(f'Old: {self.oldWords}')

    def byes(self):  # Кнопка New Word
        self.stepBtn.setEnabled(True)
        self.flag.append('yes')
        self.b += 1
        self.left_numLbl.setText(str(len(self.words) - self.b))
        self.behind_numLbl.setText(str(self.b))
        print(
            f"{(self.x + 1) * 100 // len(self.words)}% | {self.x + 1} | {self.i} ~~~ is unknown"
        )
        self.progressBar.setValue((self.x + 1) * 100 // len(self.words))
        self.newWords.append(
            f"{self.i} ~ {self.translatedWords[self.x]}".rstrip('\n'))
        if self.x + 1 < len(self.words):
            self.x += 1
            self.i = self.words[self.x]
            # Форматтер шрифта на случай длинного слова
            if len(self.words[self.x]) > 15:
                self.originalLabel.setFont(QFont('Tempus Sans ITC', 20))
            else:
                self.originalLabel.setFont(QFont('Tempus Sans ITC', 36))
            self.originalLabel.setText(self.words[self.x])
            if len(self.translatedWords[self.x]) > 12:
                self.translatedLabel.setFont(QFont('Tempus Sans ITC', 28))
            else:
                self.translatedLabel.setFont(QFont('Tempus Sans ITC', 36))
            self.translatedLabel.setText(self.translatedWords[self.x])
            # Смена слов в столбике посередине
            if self.x < 3:
                self.word_3.setText('')
            else:
                self.word_3.setText(self.words[self.x - 3])
            if self.x < 2:
                self.word_2.setText('')
            else:
                self.word_2.setText(self.words[self.x - 2])
            if self.x < 1:
                self.word_1.setText('')
            else:
                self.word_1.setText(self.words[self.x - 1])

            self.word0.setText(self.i)

            if self.x >= len(self.words) - 1:
                self.word1.setText('')
            else:
                self.word1.setText(self.words[self.x + 1])
            if self.x >= len(self.words) - 2:
                self.word2.setText('')
            else:
                self.word2.setText(self.words[self.x + 2])
            if self.x >= len(self.words) - 3:
                self.word3.setText('')
            else:
                self.word3.setText(self.words[self.x + 3])
        else:
            self.end(
            )  # В случае окончания списка слов вызов функции почти завершающей работу программы
            return

    def bno(self):  # Функция кнопки Old Word
        self.stepBtn.setEnabled(True)
        self.flag.append('no')
        self.b += 1
        self.left_numLbl.setText(str(len(self.words) - self.b))
        self.behind_numLbl.setText(str(self.b))
        print(
            f"{(self.x + 1) * 100 // len(self.words)}% | {self.x + 1} | {self.i} ~~~ is known"
        )
        self.progressBar.setValue((self.x + 1) * 100 // len(self.words))
        self.oldWords.append(self.i)
        if self.x + 1 < len(self.words):
            self.x += 1
            self.i = self.words[self.x]
            # Форматтер шрифта на случай длинного слова
            if len(self.words[self.x]) > 15:
                self.originalLabel.setFont(QFont('Tempus Sans ITC', 30))
            else:
                self.originalLabel.setFont(QFont('Tempus Sans ITC', 36))
            self.originalLabel.setText(self.words[self.x])
            if len(self.translatedWords[self.x]) > 12:
                self.translatedLabel.setFont(QFont('Tempus Sans ITC', 28))
            else:
                self.translatedLabel.setFont(QFont('Tempus Sans ITC', 36))
            self.translatedLabel.setText(self.translatedWords[self.x])
            # Смена слов в столбике посередине
            if self.x < 3:
                self.word_3.setText('')
            else:
                self.word_3.setText(self.words[self.x - 3])
            if self.x < 2:
                self.word_2.setText('')
            else:
                self.word_2.setText(self.words[self.x - 2])
            if self.x < 1:
                self.word_1.setText('')
            else:
                self.word_1.setText(self.words[self.x - 1])

            self.word0.setText(self.i)

            if self.x >= len(self.words) - 1:
                self.word1.setText('')
            else:
                self.word1.setText(self.words[self.x + 1])
            if self.x >= len(self.words) - 2:
                self.word2.setText('')
            else:
                self.word2.setText(self.words[self.x + 2])
            if self.x >= len(self.words) - 3:
                self.word3.setText('')
            else:
                self.word3.setText(self.words[self.x + 3])
        else:
            self.end(
            )  # В случае окончания списка слов вызов функции почти завершающей работу программы
            return

    def end(self):  # Функция которая приводит программу к финалу
        self.originalLabel.setText('[No words left]')
        self.translatedLabel.setText('')
        self.newBtn.setEnabled(False)
        self.oldBtn.setEnabled(False)
        self.stepBtn.setEnabled(False)
        self.manualBtn.setEnabled(False)
        outnew.write('\n'.join(self.newWords))
        outold.write('\n'.join(self.oldWords))
        self.close()
        import finalwindow  # Подключения модуля с окном обратной связи
        print('bye))')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    app.exec_()

# Закрытие файлов

f.close()
outnew.close()
outold.close()
translated.close()
