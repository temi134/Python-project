from tkinter import *

window = Tk()

window.title("Area Calculator")
window.geometry('500x500')
window.configure(bg='white')

def area():
    length = int(entry1.get())
    width = int(entry2.get())
    result = length * width
    label3.configure(text=result)

label1 = Label(window, text='Area Calculator')
label1.place(x=200, y=100)

label2 = Label(window, text='Length')
label2.place(x=100, y=175)

entry1 = Entry(window, width=10)
entry1.place(x=200, y=175)

label4 = Label(window, text='Width')
label4.place(x=100, y=225)

entry2 = Entry(window, width=10)
entry2.place(x=200, y=225)

button1 = Button(window, text='Calculate Area',
                 fg='blue', command=area)
button1.place(x=200, y=275)

label5 = Label(window, text='Area:')
label5.place(x=100, y=325)

label3 = Label(window, text='')
label3.place(x=200, y=325)

window.mainloop()