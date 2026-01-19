import random
import pgzrun

WIDTH=600
HEIGHT=508
TITLE='clicker game'
pikachu = Actor('pikachu')
pikachu.pos= (300,300)
character = Actor('character')
character.pos = (100,100)
def draw():
    screen.blit('background2',(0,0))
    pikachu.draw()
    character.draw()
    screen.draw.text(str(score),center=(30,20))
    screen.draw.text(shot,center=(30,60))
score = 0
shot = ''

def update():
    global shot
    if keyboard.left:
        character.x -= 10
    elif keyboard.right:
        character.x += 10
    elif keyboard.up:
        character.y -= 10
    elif keyboard.down:
        character.y += 10
    if character.colliderect(pikachu):
        shot = 'caught it'
    


def on_mouse_down(pos): 
    global score
    global shot
    if pikachu.collidepoint(pos) :
        pikachu.pos= (random.randint(0,600), (random.randint(0,508)))
        score = score + 1
        shot = 'good shot'
    else:
        shot = 'bad shot'
        score = score - 1




        

pgzrun.go()