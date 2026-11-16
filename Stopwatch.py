from tkinter import *
import time

window = Tk()

window.title('Stopwatch')
window.geometry('400x400')
window.configure(bg='white')

H = StringVar()
M = StringVar()
S = StringVar()

def countdown():
    Hours = int(Entry1.get())
    Minutes = int(Entry2.get())
    Seconds = int(Entry3.get())

    Total_time = Hours*3600 + Minutes*60 + Seconds

    while Total_time >= 0:
        Total_time -= 1
        if Seconds > 0:
            
            Seconds = Seconds - 1

        if Seconds == 0 and Minutes == 0 and Hours > 0:

            Hours -= 1
            Minutes = 59

        elif Minutes > 0 and Seconds == 0:
            Minutes -= 1
            Seconds = 59

        elif Hours == 0 and Minutes == 0 and Seconds == 0:
            Total_time = -1

        H.set(f'{Hours}:')
        M.set(f'{Minutes}:')
        S.set(f'{Seconds}')
        window.update()
        time.sleep(1)




label1 = Label(window,text='Choose your time')
label1.place(x=100,y=100)

Button1 = Button(window,text='Start',command=countdown)
Button1.place(x=100,y=150)

Entry1 = Entry(window,width=5)
Entry1.place(x=100,y=250)

Entry2 = Entry(window,width=5)
Entry2.place(x=150,y=250)

Entry3 = Entry(window, width=5)
Entry3.place(x=200,y=250)

label2 = Label(window,text='Hours')
label2.place(x=100,y=200)

label3 = Label(window,text='Minutes')
label3.place(x=150,y=200)

label4 = Label(window, text='Seconds')
label4.place(x=200,y=200)

label5 = Label(window,text='00:',font=('Arial',20,'bold'),textvariable=H)
label5.place(x=100,y=20)

label6 = Label(window,text='00:',font=('Arial',20,'bold'),textvariable=M)
label6.place(x=150,y=20)

label7 = Label(window,text='00',font=('Arial',20,'bold'),textvariable=S)
label7.place(x=200,y=20)

window.mainloop()