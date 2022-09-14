from tkinter import *

entry = ''

def add_text(a):
    global entry
    entry += str(a)
    entryField.delete('1.0', 'end')
    entryField.insert('1.0', entry)

window = Tk()
window.geometry('500x500')
window.title('Calculator')

entryField = Text(window, width=61, height=5)
entryField.grid(row=1,column=1, columnspan=4)

one = Button(window, text='1', command=lambda: add_text(1))
one.grid(row=2,column=1)

two = Button(window, text='2', command=lambda: add_text(2))
two.grid(row=2, column=2)

three = Button(window, text='3')
three.grid(row=2,column=3)

four = Button(window, text='4')
four.grid(row=2,column=4)

window.mainloop()