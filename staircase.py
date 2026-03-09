import pgzrun

WIDTH = 500
HEIGHT = 500

person = Actor('person')
person.pos = (100, 300)

def draw():
    screen.blit('stairs_bg',(0,0))
    person.draw()

def climb_up():
    animate(person, x = person.x + 60, y = person.y - 40, duration = 0.7, on_finished = climb_up)

def on_mouse_down():
    climb_up()

climb_up()
pgzrun.go()