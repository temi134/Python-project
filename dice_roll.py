
from tkinter import *
import random

window = Tk()

window.title("Dice Roller")
window.geometry("500x500")
window.configure(bg="white")


def roll_dice():
    number = random.randint(1, 6)

    if number == 6:
        window.configure(bg="red")
        label1.configure(text=str(number), bg="red", fg="white")
    else:
        window.configure(bg="white")
        label1.configure(text=str(number), bg="white", fg="black")


label1 = Label(window,text="0",font=("Arial", 100, "bold"),bg="white",fg="black")
label1.pack()

button1 = Button(window,text="Roll Dice",font=("Arial", 18),command=roll_dice)
button1.pack()

window.mainloop()
