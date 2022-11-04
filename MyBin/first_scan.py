#import os
import sys

from deep_translator import GoogleTranslator

import myfuncts as mf

testRunFlag = mf.testRunFlag
testPrecentageFlag = mf.testPrecentageFlag
testByeFlag = mf.testByeFlag
translateFunctionsMode = mf.translateFunctionsMode
testPtintWordsFlag = mf.testPtintWordsFlag

mf.testPrint('SCAN STARTED', testRunFlag)


def tran(to_translate):
    if translateFunctionsMode:
        return GoogleTranslator(source='en',
                                target='ru').translate(to_translate)
    return to_translate


f = open('text.txt')
out = open('res.txt', 'w')
out2 = open('word_list.txt', 'w')
out_tr = open('translated_list.txt', 'w', encoding='utf-8')

st = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
st2 = '"?!/.,:;()*@~`{[}]<>_-—+= '
words = set([])
word = ''

entireText = f.readlines()

for i in entireText:
    for j in i + ' ':
        if j in st2:
            if word != ' ' and word != '':
                words.add(word.lower())
                word = ''
        else:
            if j in st:
                word += j

words = list(words)
words.sort()
mf.testPrint(words, testPtintWordsFlag)
i = 0

x = len(words)

if not x:
    print('ERROR: YOU DONT HAVE ANY TEXT')
    sys.exit()
while i < len(words) - 1:

    if words[i] + 's' == words[i + 1] or words[i] + 'es' == words[i + 1]:
        words.pop(i + 1)
        i -= 2

    if words[i] + 'd' == words[i + 1] or words[i] + 'ed' == words[i + 1]:
        words.pop(i + 1)
        i -= 2

    if words[i] + 'ing' == words[i + 1]:
        words.pop(i + 1)
        i -= 2

    if words[i] + 'er' == words[i + 1]:
        words.pop(i + 1)
        i -= 2

    if words[i] + 'ly' == words[i + 1]:
        words.pop(i + 1)
        i -= 2

    i += 1

#translator= Translator(to_lang="ru")

x = 0
for i in words:

    #print(x / len(words) * 100, end = '')
    x += 1
    mf.testPrint(f"{x * 100 // len(words)}% | {x} | {i}", testPrecentageFlag)

    #out.writelines(i + ' ' + translator.translate(i) + '\n')
    out.writelines(i + '\n')
    out2.writelines(i + '\n')
    out_tr.writelines(tran(i) + '\n')
    #print(tran(i))

mf.testPrint(words, testPtintWordsFlag)

if len(words) == 0:
    pass
    # LATER I have to add something

# os.startfile(r'second_scan.py')
f.close()
out.close()
out2.close()
out_tr.close()

mf.testPrint('bye))', testByeFlag)
