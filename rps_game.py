from tkinter import *
import random

window = Tk()

window.geometry('500x500')
window.configure(bg='white')
choice = ''
Computers_choice = ''
Score = 0
Computers_score = 0

def rock():
    global choice
    choice = 'rock'
    winner()

def paper():
    global choice
    choice = 'paper'
    winner()

def scissors():
    global choice
    choice = 'scissors'
    winner()

def winner():
    global choice 
    global Computers_choice
    global Score
    global Computers_score
    Computers_choice = random.choice(['rock','paper','scissors'])
    label4.configure(text='Your choice: '+choice)
    label3.configure(text='Computers choice: '+Computers_choice)
  
    if choice == 'rock' and Computers_choice == 'paper':
        label2.configure(text='computer wins')
        Computers_score = Computers_score + 1
    elif choice == 'paper' and Computers_choice == 'rock':
        label2.configure(text='You win')
        Score = Score + 1
    elif choice == 'scissors' and Computers_choice == 'paper':
        label2.configure(text='You win')
        Score = Score + 1
    elif choice == 'paper' and Computers_choice == 'scissors':
        label2.configure(text='computer wins')
        Computers_score = Computers_score + 1
    elif choice == 'rock' and Computers_choice == 'scissors':
        label2.configure(text='You win')
        Score = Score + 1
    elif choice == 'scissors' and Computers_choice == 'rock':
        label2.configure(text='computer wins')
        Computers_score = Computers_score + 1
    elif choice == Computers_choice:
        label2.configure(text='draw')
    label5.configure(text='Your score: '+str(Score))
    label6.configure(text='Computers score: '+ str(Computers_score))
        




label1 = Label(window, text='Rock Paper Scissors',font=('Arial',25))
label1.place(x=100,y=100)

label2 = Label(window, text='winner')
label2.place(x=200,y=250)

button1 = Button(window, text='rock' ,command=rock)
button1.place(x=100,y=200)

button2 = Button(window,text='scissors' ,command=scissors)
button2.place(x=200,y=200)

button3 = Button(window,text='paper' ,command=paper)
button3.place(x=300,y=200)

label4 = Label(window,text='choice')
label4.place(x=100,y=300)

label3 = Label(window,text='Computers_choice')
label3.place(x=300,y=300)

label5 = Label(window, text='Your Score')
label5.place(x=50,y=50)

label6 = Label(window, text='Computers score')
label6.place(x=350, y = 50)

window.mainloop()

