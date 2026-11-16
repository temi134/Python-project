from tkinter import *

window = Tk()
window.title("Warning Alert")
window.geometry("400x300")
window.configure(bg="white")

label1 = Label(window, text="WARNING!", fg="red", bg="white", font=("Arial", 25, "bold"))
label1.pack(pady=100)

colour = "red"

def flash():
    global colour

    if colour == "red":
        label1.configure(fg="white")
        colour = "white"
    else:
        label1.configure(fg="red")
        colour = "red"

    window.after(500, flash)

flash()

window.mainloop()