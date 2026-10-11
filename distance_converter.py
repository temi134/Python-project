from tkinter import *

window = Tk()

window.geometry('500x500')
window.configure(bg='white')

def distance():
    distance= int(entry1.get())
    distance_m= (distance/10)
    distance_km = (distance/1000)
    distance_miles = (distance/160934.4)
    label2.configure(text=distance_m)
    label4.configure(text=distance_km)
    label5.configure(text=distance_miles)

label1 = Label(window, text='distance converter')
label1.place(x=175 , y=100)

button1 = Button(window, text='convert', fg='blue', command=distance)
button1.place(x=300 , y=175)

label2 = Label(window, text='metres')
label2.place(x=100, y=250)

label3 = Label(window, text='distance in cm')
label3.place(x=100, y=175)

entry1 = Entry(window,width = 10)
entry1.place(x=200 ,y=175)

label4 = Label(window,text='kilometers')
label4.place(x=200,y=250)

label5 = Label(window, text='miles')
label5.place(x=300,y=250)

label6 = Label(window, text='metres')
label6.place(x=100 , y=300)

label7 = Label(window,text='kilometres')
label7.place(x=200,y=300)

label8 = Label(window,text='miles')
label8.place(x=300,y=300)
window.mainloop()