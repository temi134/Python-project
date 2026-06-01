import pgzrun

HEIGHT = 500
WIDTH = 500

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw_circle(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

circle1 = Circle(200, 200, 30, 'white')
circle2 = Circle(100, 300, 60, 'red')

def draw():
    screen.clear()
    circle1.draw_circle()
    circle2.draw_circle()

speed = 1

def update():
    global speed

    
    circle1.y = circle1.y + speed
    circle1.x = circle1.x + 1

    if circle1.y >= 200:
        speed = -1

    elif circle1.y <= 100:
        speed = 1

pgzrun.go()


 


    