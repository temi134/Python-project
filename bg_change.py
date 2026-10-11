from tkinter import *

window = Tk()

window.geometry('500x500')
window.configure(bg='black')

def red():
    window.configure(bg='red')
    label1.config(text='Stop', fg='white', bg='red')

def yellow():
    window.configure(bg='yellow')
    label1.config(text='Go slow', fg='black', bg='yellow')

def green():
    window.configure(bg='green')
    label1.config(text='Go', fg='white', bg='green')

label1 = Label(window, text='hello')
label1.place(x=100, y=100)

button1 = Button(window, text='Red', fg='red', command=red)
button1.place(x=150, y=250)

button2 = Button(window, text='Yellow', fg='yellow', command=yellow)
button2.place(x=220, y=250)

button3 = Button(window, text='Green', fg='green', command=green)
button3.place(x=300, y=250)

window.mainloop()