#import docx
#from translate import Translator
from tkinter import*
from tkinter import scrolledtext

print('TRUE FILE OPENED')

f = open('word_list.txt')
outnew = open('new.txt', 'w')
outold = open('notnew.txt', 'w')


st = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
st2 = '"?!/.,:;()*@~`{[}]<>_-—+= '
words = set([])
word = ''

for i in f.readlines():
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

#GUI ALG:

x = 0
b = 0
i = ''

def main():
    global x
    x = 0
    global i
    i = words[x]

lel = len(words)
main()

def unb(event):
    pass

def end():
    lbl.configure(text = "Все слова отсортированы :)", fg = 'lime')
#     words_left.configure(text=f"Осталось слов: {len(words) - 0}")
#     yesb['state'] = DISABLED
#     nob['state'] = DISABLED
    words_left.destroy()
    yesb.destroy()
    nob.destroy()
    window.bind('<Left>', unb)
    window.bind('<Right>', unb)
    print('bye))')


def cyes(event):
    global b
    global x
    global i
    b += 1
    words_left.configure(text=f"Осталось слов: {len(words) - b}")
    print(f"{(x + 1) * 100 // len(words)}% | {x + 1} | {i} ~~~ is unknown")
#         window.destroy()
    outnew.writelines(i + '\n')
    if x + 1< len(words):
        x += 1
        i = words[x]
        lbl.configure(text=i)
    else:
        end()
        return


def cno(event):
    global b
    global x
    global i
    b += 1
    words_left.configure(text=f"Осталось слов: {len(words) - b}")
    print(f"{(x + 1) * 100 // len(words)}% | {x + 1} | {i} ~~~ is unknown")
#         window.destroy()
    outold.writelines(i + '\n')
    if x + 1< len(words):
        x += 1
        i = words[x]
        lbl.configure(text=i)
    else:
        end()
        return
    
    
def byes():
    global b
    global x
    global i
    b += 1
    words_left.configure(text=f"Осталось слов: {len(words) - b}")
    print(f"{(x + 1) * 100 // len(words)}% | {x + 1} | {i} ~~~ is unknown")
#         window.destroy()
    outnew.writelines(i + '\n')
    if x + 1< len(words):
        x += 1
        i = words[x]
        lbl.configure(text=i)
    else:
        end()
        return


def bno():
    global b
    global x
    global i
    b += 1
    words_left.configure(text=f"Осталось слов: {len(words) - b}")
    print(f"{(x + 1) * 100 // len(words)}% | {x + 1} | {i} ~~~ is unknown")
#         window.destroy()
    outold.writelines(i + '\n')
    if x + 1< len(words):
        x += 1
        i = words[x]
        lbl.configure(text=i)
    else:
        end()
        return

def copytg():
    copyb.clipboard_clear()
    copyb.clipboard_append('@timacdc')

window = Tk()
window.title("Фильтр слов")  
lbl = Label(window, text=i, font=("Arial Bold", 50)) 
lbl.grid(column=0, row=0, columnspan=2)
yesb = Button(window, text="NEW", command=byes, bg = 'green', fg = 'black', font=("Arial Bold", 100))
nob = Button(window, text="OLD", command=bno, bg = 'red', fg = 'black', font=("Arial Bold", 100))
window.bind('<Left>', cyes)
window.bind('<Right>', cno)
yesb.grid(column=0, row=1)
nob.grid(column=1, row=1)
words_left = Label(window, text=f"Осталось слов: {lel - b}", font=("Arial Bold", 50)) 
words_left.grid(column=0, row=2, columnspan=2)
# titles = Label(window, text="Телеграм автора", font=("Arial Bold", 15), bg = 'royalblue', fg = 'white') 
# titles.grid(column=0, row=3)
copyb = Button(window, text = 'Телеграм автора: @timacdc - нажмите чтобы скопировать', font = ("Arial Bold", 15), command=copytg, bg = 'royalblue', fg = 'white')
copyb.grid(column=0, row=3, columnspan = 2)
window.resizable(0,0)
window.mainloop()
    
print('PROGRAMM FINISHED')

