#import os
import sys
import time

from deep_translator import GoogleTranslator
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow

import myfuncts as mf

print('SCAN STARTED')


class MyWidget1(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('loading.ui', self)
        '''flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)'''
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.progressBar.setValue(0)
        self.testRunFlag = mf.testRunFlag
        self.testPrecentageFlag = mf.testPrecentageFlag
        self.testByeFlag = mf.testByeFlag
        self.translateFunctionsMode = mf.translateFunctionsMode
        self.testPtintWordsFlag = mf.testPtintWordsFlag
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

    def tran(self, to_translate):
        if self.translateFunctionsMode:
            return GoogleTranslator(source='en',
                                    target='ru').translate(to_translate)
        return to_translate

    def main(self):
        self.pushButton.hide()
        for self.i in self.entireText:
            for self.j in self.i + ' ':
                if self.j in self.st2:
                    if self.word != ' ' and self.word != '':
                        self.words.add(self.word.lower())
                        self.word = ''
                else:
                    if self.j in self.st:
                        self.word += self.j

        self.words = list(self.words)
        self.words.sort()
        mf.testPrint(self.words, self.testPtintWordsFlag)
        self.i = 0

        self.x = len(self.words)

        if not self.x:
            print('ERROR: YOU DONT HAVE ANY TEXT')
            sys.exit()
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

        #translator= Translator(to_lang="ru")

        self.x = 0

        for self.i in self.words:

            #print(x / len(self.words) * 100, end = '')
            self.x += 1
            print(f"{self.x * 100 // len(self.words)}% | {self.x} | {self.i}")
            self.label_file.setText(self.i)
            self.progressBar.setValue((self.x) * 100 // len(self.words))

            #out.writelines(self.i + ' ' + translator.translate(self.i) + '\n')
            self.out.writelines(self.i + '\n')
            self.out2.writelines(self.i + '\n')
            self.out_tr.writelines(self.tran(self.i) + '\n')
            #print(tran(self.i))
        self.label_file.setText('Process completed successfully')
        print(self.words)

        self.f.close()
        self.out.close()
        self.out2.close()
        self.out_tr.close()

        time.sleep(1)
        self.close()

        print('bye))')


app = QApplication(sys.argv)
ex = MyWidget1()
ex.show()
app.exec_()
