from tkinter import *
import random

window = Tk()

window.title('Lucky Slots')
window.geometry('400x400')
window.configure(bg='white')


def spin():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)

    label1.configure(text=str(num1))
    label2.configure(text=str(num2))
    label3.configure(text=str(num3))

    if num1 == num2 == num3:
        label4.configure(text='JACKPOT! You win $1000!')

    elif num1 == num2 or num1 == num3 or num2 == num3:
        label4.configure(text='Mini Prize! You win $10!')

    else:
        label4.configure(text='Bad Luck! Try Again.')


label1 = Label(window, text='0', font=('Arial', 30))
label1.place(x=70, y=100)

label2 = Label(window, text='0', font=('Arial', 30))
label2.place(x=170, y=100)

label3 = Label(window, text='0', font=('Arial', 30))
label3.place(x=270, y=100)

Button1 = Button(window, text='SPIN', command=spin)
Button1.place(x=170, y=200)

label4 = Label(window, text='Press SPIN to play')
label4.place(x=120, y=270)

window.mainloop()