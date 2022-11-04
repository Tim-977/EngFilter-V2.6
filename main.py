import sys

from deep_translator import GoogleTranslator
from PyQt5 import uic
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QBrush, QFont, QImage, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

import myfuncts as mf

#import pyManual as pm

showManual = mf.showManual

#TODO:
# 1.Add untranslatable words list
# 2.Make own dictionary (SQL)
# 3.Add nice UI
# 4.Make loading bar

# Открытие необходимых файлов
# И создание необходимых необходимостей

doScan = mf.doScan

if doScan:
    print('Do a new scan?\ny/n?')

    while True:
        choise = input()
        if choise.lower() == 'y':
            import first_scan
            break
        elif choise.lower() == 'n':
            print('Ok')
            break
        else:
            print('please, type Y or N')
            continue

testFlag1 = mf.testFlag1
testFlag2 = mf.testFlag2

f = open('word_list.txt')
outnew = open('new.txt', 'w', encoding='utf-8')
outold = open('notnew.txt', 'w')
translated = open('translated_list.txt', 'r', encoding='utf-8')

st = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
st2 = '"?!/.,:;()*@~`{[}]<>_-—+= '
words = set([])
word = ''
i = ''

# Цикл, делающий множество слов words

for i in f.readlines():
    for j in i + ' ':
        if j in st2:
            if word != ' ' and word != '':
                words.add(word.lower())
                mf.testPrint(f"w: {words}", testFlag1)
                word = ''

        else:
            if j in st:
                word += j

# Делаем из множества массив и сортируем

words = list(words)
words.sort()
mf.testPrint(f"WORDS: {words}", testFlag2)

if not len(words):
    print('ERROR: YOU DONT HAVE ANY TEXT')
    sys.exit()


class Window2(QWidget):

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


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('EngFilUi.ui', self)
        oImage = QImage("Pics\\bgframe.png")
        sImage = oImage.scaled(QSize(903, 679))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.stepBackFlag = mf.stepBackFlag
        self.stepBackFlagNew = mf.stepBackFlagNew
        self.stepBackFlagOld = mf.stepBackFlagOld
        self.testBnoFlag = mf.testBnoFlag
        self.testByesFlag = mf.testByesFlag
        self.testBnoFlag = mf.testBnoFlag
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
        #self.translatedLabel.setText('[перевод слова]')
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
        # self.newBtn.setStyleSheet("color: green; background-image: url(frame4.png);")
        # self.oldBtn.setStyleSheet("color: red; background-image: url(frame4.png);")
        self.stepBtn.setEnabled(False)
        self.stepBtn.clicked.connect(self.stepback)
        self.originalLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.translatedLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.word_3.setStyleSheet("color: #C0C0C0;")
        self.word_2.setStyleSheet("color: #909090;")
        self.word_1.setStyleSheet("color: #606060;")
        self.word0.setStyleSheet("color: #000000;")
        self.word1.setStyleSheet("color: #606060;")
        self.word2.setStyleSheet("color: #909090;")
        self.word3.setStyleSheet("color: #C0C0C0;")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D and len(self.words) - self.b != 0:
            self.byes()
        if event.key() == Qt.Key_A and len(self.words) - self.b != 0:
            self.bno()
        if event.key() == Qt.Key_Z and len(
                self.flag) > 0 and len(self.words) - self.b != 0:
            self.stepback()
        if event.key() == Qt.Key_F1 and len(self.words) - self.b != 0:
            self.window2()

    def window2(self):
        self.w = Window2()
        self.w.show()

    def tran(self, to_translate):
        return GoogleTranslator(source='en',
                                target='ru').translate(to_translate)

    def stepback(self):
        if len(self.flag) == 1:
            self.stepBtn.setEnabled(False)
        self.x -= 1
        self.b -= 1
        self.i = self.words[self.x]
        self.left_numLbl.setText(str(len(self.words) - self.b))
        self.behind_numLbl.setText(str(self.b))
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
        mf.testPrint('Stepped back', self.stepBackFlag)
        mf.testPrint(f'New: {self.newWords}', self.stepBackFlagNew)
        mf.testPrint(f'Old: {self.oldWords}', self.stepBackFlagOld)

    def byes(self):
        self.stepBtn.setEnabled(True)
        self.flag.append('yes')
        self.b += 1
        self.left_numLbl.setText(str(len(self.words) - self.b))
        self.behind_numLbl.setText(str(self.b))
        mf.testPrint(
            f"{(self.x + 1) * 100 // len(self.words)}% | {self.x + 1} | {self.i} ~~~ is unknown",
            self.testByesFlag)
        self.progressBar.setValue((self.x + 1) * 100 // len(self.words))
        #outnew.writelines(self.i + '\n')
        self.newWords.append(
            f"{self.i} ~ {self.translatedWords[self.x]}".rstrip('\n'))
        if self.x + 1 < len(self.words):
            self.x += 1
            self.i = self.words[self.x]
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
            # self.originalLabel.setText(self.i)
            # self.translatedLabel.setText(self.translatedWords[self.x])
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
            self.end()
            return

    def bno(self):
        self.stepBtn.setEnabled(True)
        self.flag.append('no')
        self.b += 1
        self.left_numLbl.setText(str(len(self.words) - self.b))
        self.behind_numLbl.setText(str(self.b))
        mf.testPrint(
            f"{(self.x + 1) * 100 // len(self.words)}% | {self.x + 1} | {self.i} ~~~ is known",
            self.testBnoFlag)
        self.progressBar.setValue((self.x + 1) * 100 // len(self.words))
        #outold.writelines(self.i + '\n')
        self.oldWords.append(self.i)
        if self.x + 1 < len(self.words):
            self.x += 1
            self.i = self.words[self.x]
            #self.originalLabel.setText(self.i)
            #self.translatedLabel.setText(self.translatedWords[self.x])
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
            self.end()
            return

    def end(self):
        self.originalLabel.setText('[No words left]')
        self.translatedLabel.setText('')
        self.newBtn.setEnabled(False)
        self.oldBtn.setEnabled(False)
        self.stepBtn.setEnabled(False)
        self.manualBtn.setEnabled(False)
        outnew.write('\n'.join(self.newWords))
        outold.write('\n'.join(self.oldWords))
        self.close()
        import finalwindow
        mf.testPrint('bye))', self.testByesFlag)


if True:
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    app.exec_()

f.close()
outnew.close()
outold.close()
translated.close()
