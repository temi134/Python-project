from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title('Multiplication table')
window.geometry('400x400')

def Multiply():
    Value = Number.get()
    label2.configure(text=Value)


label1 = Label(window,text='Multiplication table')
label1.place(x=200,y=20)

label2 = Label(window,text='')
label2.place(x=20,y=100)

button1 = Button(window,text='Multiply',command=Multiply)
button1.place(x=20,y=150)

Num = IntVar()

Number = Combobox(window,textvariable=Num)
Number.place(x=200,y=150)

Number['values']=tuple(range(20))

window.mainloop()