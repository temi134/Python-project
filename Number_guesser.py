from tkinter import *
import random

window= Tk()

window.title('Number Guesser')
window.geometry('400x400')
window.configure(bg='white')
number = random.randint(1,10)
print(number)
Chances = 3
Score = 0

def check_number():
    global number
    global Chances
    global Score
    guess = int(entry1.get())

    if Chances <= 0:
        label2.configure(text='You lost it is a new number now')
        Chances = 3
        number = random.randint(1,10)
        label3.configure(text='Hint')
        label4.configure(text='Chances'+str(Chances))

    if number == guess and Chances > 0:
        label2.configure(text='you got it right')
        number = random.randint(1,10)
        label3.configure(text='Hint:')
        print(number)
        Chances = 3
        label4.configure(text='Chances'+str(Chances))
        Score = Score + 1

    elif number > guess:
        label2.configure(text='Try again')
        label3.configure(text='Hint: Your number is too small')
        Chances = Chances - 1
        label4.configure(text='Chances'+str(Chances))
        
        if Chances <= 0:
            label2.configure(text='You lost it is a new number now')
            Chances = 3
            number = random.randint(1,10)
            label3.configure(text='Hint')
            label4.configure(text='Chances'+str(Chances))
            
    elif number < guess:
        label2.configure(text='Try again')
        label3.configure(text='Hint: Your number is too big')
        Chances = Chances - 1
        label4.configure(text='Chances'+str(Chances))
        
        if Chances <= 0:
            label2.configure(text='You lost it is a new number now')
            Chances = 3
            number = random.randint(1,10)
            label3.configure(text='Hint')
            label4.configure(text='Chances'+str(Chances))

label1 = Label(window,text='Number Guesser')
label1.place(x=150, y=50)

label2 = Label(window,text='Guess any number')
label2.place(x=150, y=100)

entry1 = Entry(window,width=5)
entry1.place(x=150, y=150)

Button1 = Button(window,text='Check your answer',command=check_number)
Button1.place(x=150,y=200)

label3 = Label(window, text='hint')
label3.place(x=150,y=250)

label4 = Label(window,text='Chances:'+str(Chances))
label4.place(x=150,y=300)

label5 = Label(window, text='Score:'+str(Score))
label5.place(x=150, y=350)
window.mainloop()