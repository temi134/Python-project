from tkinter import *

window = Tk()

window.geometry('500x500')

window.configure(bg = 'black')

def change():
    label1.config(text='bye')
    label1.config(fg='blue',bg='sky blue')


button1 = Button(window, text = 'change',command=change)

button1.place(x=250,y=250)

label1 = Label(window,text='hello')

label1.place(x=100,y=100)

window.mainloop()