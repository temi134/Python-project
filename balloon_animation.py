import pgzrun

WIDTH = 740
HEIGHT = 416

ship = Actor('ship')
ship.angle = -15
ship.pos = (100,300)

def draw():
    screen.blit('waves',(0,0))
    ship.draw()

    
def ship_up():
    animate(ship,angle = ship.angle+30,x = ship.x + 30 ,  y = 260 , duration = 1 , on_finished = ship_down )

def ship_down():
    animate(ship,angle = ship.angle-30, x = ship.x + 30 , y = 300 , duration = 1 , on_finished = ship_up) 



ship_up()



pgzrun.go()


