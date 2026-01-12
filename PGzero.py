import pgzrun

HEIGHT=329
WIDTH=600
TITLE='Game'
spongebob = Actor('character')
spongebob.pos= (300,300)
def draw():
    screen.blit('landscape',(0,0))
    spongebob.draw()

pgzrun.go()
