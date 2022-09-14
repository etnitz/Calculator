from tkinter import *

entry = ''

def add_text(a):
    global entry
    entry += str(a)
    entry_field.delete('1.0', 'end')
    entry_field.insert('1.0', entry)

def calc():
    global entry
    result = eval(entry)
    entry_field.delete('1.0', 'end')
    entry_field.insert('1.0', result)

def clear_screen():
    global entry
    entry = ''
    entry_field.delete('1.0','end')

window = Tk()
window.geometry('555x405')
window.title('Calculator')
window.configure(bg='#5c5959')

entry_field = Text(window, width=68, height=5)
entry_field.grid(row=1,column=1, columnspan=4)

one = Button(window, text='1', command=lambda: add_text(1), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
one.grid(row=4, column=1)

two = Button(window, text='2', command=lambda: add_text(2), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
two.grid(row=4, column=2)

three = Button(window, text='3', command=lambda: add_text(3), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
three.grid(row=4, column=3)

four = Button(window, text='4',command=lambda: add_text(4), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
four.grid(row=3, column=1)

five = Button(window, text='5', command=lambda: add_text(5), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
five.grid(row=3, column=2)

six = Button(window, text='6', command=lambda: add_text(6), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
six.grid(row=3, column=3)

seven = Button(window, text='7', command=lambda: add_text(7), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
seven.grid(row=2, column=1)

eight = Button(window, text='8', command=lambda: add_text(8), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
eight.grid(row=2, column=2)

nine = Button(window, text='9', command=lambda:add_text(9), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
nine.grid(row=2, column=3)

zero = Button(window, text='0', command=lambda: add_text(0), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
zero.grid(row=5, column=2)

add = Button(window, text='+', command=lambda: add_text('+'), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
add.grid(row=5, column=4)

sub = Button(window, text='-', command=lambda: add_text('-'), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
sub.grid(row=4, column=4)

mult = Button(window, text='*', command=lambda: add_text('*'), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
mult.grid(row=3, column=4)

div = Button(window, text='/', command=lambda: add_text('/'), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
div.grid(row=2, column=4)

lp = Button(window, text='(', command=lambda: add_text('('), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
lp.grid(row=6, column=1)

rp = Button(window, text=')', command=lambda: add_text(')'), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
rp.grid(row=6, column=2)

dec = Button(window, text='.', command=lambda: add_text('.'), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
dec.grid(row=5, column=1)

equal = Button(window, text='=',command=lambda: calc(), width=22, height=2, bg='black', fg='white', font=('Times New Roman', 16))
equal.grid(row=6, column=3, columnspan=2)

clear = Button(window, text='clear', command=lambda: clear_screen(), width=10, height=2, bg='black', fg='white', font=('Times New Roman', 16))
clear.grid(row=5, column=3)

window.mainloop()