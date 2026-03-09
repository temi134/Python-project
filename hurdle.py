import pgzrun
import random 
 

WIDTH = 700
HEIGHT = 416 

pixel = Actor('pixels')
pixel.pos = (100,300)
shrubs_images = ['shrub', 'shrub2' , 'shrub3']
shrubs_list = []


def draw():
    screen.blit('plainbg',(0,0))
    pixel.draw()
    for shrub in shrubs_list:
        shrub.draw()

def on_key_down(key):
    if key == keys.SPACE and pixel.y >= 300:
        for i in range(20):
            pixel.y -= 9

def update():
    if pixel.y < 300:
        pixel.y += 3

    for shrub in shrubs_list:
        shrub.x -= 10


def hurdles():
    shrubs = Actor(random.choice(shrubs_images))
    shrubs.pos = (700,300)
    shrubs_list.append(shrubs)
    clock.schedule(hurdles,3)
    
    

hurdles()



pgzrun.go()
