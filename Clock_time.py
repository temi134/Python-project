from tkinter import *
from time import strftime

window = Tk()

window.title('clock')
window.geometry('400x400')
window.configure(bg='white')

def Clock_time():
    current_time = strftime('%H:%M:%S %p')
    label1.configure(text=current_time)
    label1.after(1000, Clock_time)


label1 = Label(window, text='', font=('Arial',30,'bold'))
label1.place(x=100,y=100)

Clock_time()

window.mainloop()