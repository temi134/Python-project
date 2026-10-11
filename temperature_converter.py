from tkinter import *

window = Tk()

window.geometry('500x500')
window.configure(bg='white')

def temp():
    temperature = int(entry1.get())
    temperature_F = (temperature*(9/5)+32)
    label3.configure(text=temperature_F)


label1 = Label(window, text='Temperature Converter')
label1.place(x=175, y=50)

label2 = Label(window, text='temperature')
label2.place(x=100 , y=100)

button1 = Button(window, text='convert', fg='blue', command=temp)
button1.place(x=300 , y=100)

entry1 = Entry(window, width=10)
entry1.place(x=200, y=100)

label3 = Label(window, text='')
label3.place(x=200, y=200)

window.mainloop()