from tkinter import *

window = Tk()

window.geometry('300x300')

window.configure(bg = 'black')

def change():
    window.configure(bg = 'sky blue')

def change2():
    window.configure(bg = 'red')


label1 = Label(window,text = 'hello', bg = 'blue', fg  = 'yellow', font = ('arial',30))

label1.place(x = 75, y = 150)

button1 = Button(window,text = 'click',bg = 'white', fg = 'black', font =('arial',30), command=change)

button1.place(x=75 , y = 20)

button2 = Button(window, text = 'click', command= change2)

button2.place(x = 200 , y = 200)









window.mainloop()