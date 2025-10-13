import turtle
import random 
import time

paper = turtle.Screen()
pen = turtle.Turtle()
paper.setup(600,600)
pen.speed(100)
paper.bgcolor('black')
pen.hideturtle()

color = ['brown','black','blue','white','red','pink','gold']

turtle.colormode(255)


def random_color():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    pen.color(r,g,b)





def circle():
    radius = random.randint(20,100)
    pen.circle(radius)

for i in range(50):
    paper.bgcolor(random.choice(color))
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    pen.up()
    pen.goto(x,y)
    pen.down()
    random_color()
    pen.begin_fill()
    circle()
    pen.end_fill()
    time.sleep(0.1)
    pen.clear()

