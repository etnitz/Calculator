from tkinter import *

entry = ''

def add_text(a):
    global entry
    entry += str(a)
    entryField.delete('1.0', 'end')
    entryField.insert('1.0', entry)

window = Tk()
window.geometry('495x495')
window.title('Calculator')

entryField = Text(window, width=61, height=5)
entryField.grid(row=1,column=1, columnspan=4)

one = Button(window, text='1', command=lambda: add_text(1))
one.grid(row=2,column=1)

two = Button(window, text='2', command=lambda: add_text(2))
two.grid(row=2, column=2)

three = Button(window, text='3', command=lambda: add_text(3))
three.grid(row=2,column=3)

four = Button(window, text='4',command=lambda: add_text(4))
four.grid(row=2,column=4)

five = Button(window, text='5', command=lambda: add_text(5))
five.grid(row=3,column=1)

six = Button(window, text='6', command=lambda: add_text(6))
six.grid(row=3,column=2)

seven = Button(window, text='7', command=lambda: add_text(7))
seven.grid(row=3,column=3)

eight = Button(window, text='8', command=lambda: add_text(8))
eight.grid(row=3,column=4)

nine = Button(window, text='9', command=lambda:add_text(9))
nine.grid(row=4,column=1)

zero = Button(window, text='0', command=lambda: add_text(0))
zero.grid(row=4,column=2)

add = Button(window, text='+', command=lambda: add_text('+'))
add.grid(row=4,column=3)

sub = Button(window, text='-', command=lambda: add_text('-'))
sub.grid(row=4,column=4)

mult = Button(window, text='*', command=lambda: add_text('*'))
mult.grid(row=5, column=1)

div = Button(window, text='/', command=lambda: add_text('/'))
div.grid(row=5, column=2)

lp = Button(window, text='(', command=lambda: add_text('('))
lp.grid(row=5,column=3)

rp = Button(window, text=')', command=lambda: add_text(')'))
rp.grid(row=5, column=4)

dec = Button(window, text='.', command=lambda: add_text('.'))
dec.grid(row=6, column=1)

equal = Button(window, text='=')
equal.grid(row=6, column=2)

clear = Button(window, text='clear')
clear.grid(row=6, column=3)

window.mainloop()