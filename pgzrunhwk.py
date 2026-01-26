import pgzrun

WIDTH = 600
HEIGHT = 508
TITLE = 'clicker game'

character = Actor('character')
character.pos = (100, 100)

def draw():
    screen.clear()
    character.draw()

def on_mouse_down(pos):
    character.pos = pos

pgzrun.go()


