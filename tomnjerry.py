import pgzrun
import random

WIDTH=600
HEIGHT=508

tom = Actor('tom_image')
jerry = Actor('jerry_image')
jerry.pos = (200,200)


def draw():
    screen.blit('background2',(0,0))
    screen.draw.text('score:'+str(score),center = (50,10))

    tom.draw()
    jerry.draw()

def move_jerry():
    global score
    x = random.randint(0,600)
    y = random.randint(0,508)
    if not jerry.colliderect(tom):
        score = score - 1
    jerry.pos = (x,y)
    clock.schedule(move_jerry,2)
    
    

score = 0

def update():
    global score
    if keyboard.right:
        tom.x += 5
    elif keyboard.left:
        tom.x -= 5
    elif keyboard.down:
        tom.y += 5
    elif keyboard.up:
        tom.y -= 5
    if tom.colliderect(jerry):
        score = score + 1
        move_jerry()





move_jerry()
pgzrun.go()