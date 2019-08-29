from tkinter import *
from tkinter import ttk


result = ''


def button_click(button):
    global result
    result += button
    result_variable.set(result)


def equals():
    global result
    total = str(eval(result))
    result_variable.set(total)


def c():
    global result
    result = ''
    result_variable.set(result)


def calculate():
    root.mainloop()


root = Tk()
root.title('Calculator')
root.geometry('240x240')

content = ttk.Frame(root)
content.grid(row=0, column=0, sticky='nsew')
content['padding'] = (5, 5)

result_variable = StringVar()

display = ttk.Entry(content, font=('Arial', 12, 'bold'), textvariable=result_variable)
display.grid(row=0, column=0, sticky='nsew', pady=2)

key_pad = ttk.Frame(content)
key_pad.grid(row=1, column=0, sticky='nsew')

c = ttk.Button(key_pad, text='C', command=c)
# ce = ttk.Button(key_pad, text='CE')
modulo = ttk.Button(key_pad, text='%', command=lambda: button_click('%'))
division = ttk.Button(key_pad, text='/', command=lambda: button_click('/'))
seven = ttk.Button(key_pad, text='7', command=lambda: button_click('7'))
eight = ttk.Button(key_pad, text='8', command=lambda: button_click('8'))
nine = ttk.Button(key_pad, text='9', command=lambda: button_click('9'))
multiplication = ttk.Button(key_pad, text='x', command=lambda: button_click('*'))
four = ttk.Button(key_pad, text='4', command=lambda: button_click('4'))
five = ttk.Button(key_pad, text='5', command=lambda: button_click('5'))
six = ttk.Button(key_pad, text='6', command=lambda: button_click('6'))
subtraction = ttk.Button(key_pad, text='-', command=lambda: button_click('-'))
one = ttk.Button(key_pad, text='1', command=lambda: button_click('1'))
two = ttk.Button(key_pad, text='2', command=lambda: button_click('2'))
three = ttk.Button(key_pad, text='3', command=lambda: button_click('3'))
addition = ttk.Button(key_pad, text='+', command=lambda: button_click('+'))
zero = ttk.Button(key_pad, text='0', command=lambda: button_click('0'))
point = ttk.Button(key_pad, text='.', command=lambda: button_click('.'))
equals = ttk.Button(key_pad, text='=', command=equals)

c.grid(row=0, column=0, columnspan=2, sticky='nsew')
# ce.grid(row=0, column=1, sticky='nsew')
modulo.grid(row=0, column=2, sticky='nsew')
division.grid(row=0, column=3, sticky='nsew')
seven.grid(row=1, column=0, sticky='nsew')
eight.grid(row=1, column=1, sticky='nsew')
nine.grid(row=1, column=2, sticky='nsew')
multiplication.grid(row=1, column=3, sticky='nsew')
four.grid(row=2, column=0, sticky='nsew')
five.grid(row=2, column=1, sticky='nsew')
six.grid(row=2, column=2, sticky='nsew')
subtraction.grid(row=2, column=3, sticky='nsew')
one.grid(row=3, column=0, sticky='nsew')
two.grid(row=3, column=1, sticky='nsew')
three.grid(row=3, column=2, sticky='nsew')
addition.grid(row=3, column=3, sticky='nsew')
zero.grid(row=4, column=0, columnspan=2, sticky='nsew')
point.grid(row=4, column=2, sticky='nsew')
equals.grid(row=4, column=3, sticky='nsew')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
key_pad.columnconfigure(0, weight=1)
key_pad.columnconfigure(1, weight=1)
key_pad.columnconfigure(2, weight=1)
key_pad.columnconfigure(3, weight=1)
key_pad.rowconfigure(0, weight=1)
key_pad.rowconfigure(1, weight=1)
key_pad.rowconfigure(2, weight=1)
key_pad.rowconfigure(3, weight=1)
key_pad.rowconfigure(4, weight=1)


if __name__ == '__main__':
    calculate()