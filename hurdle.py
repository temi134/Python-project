import pgzrun
import random 
 

WIDTH = 700
HEIGHT = 416 

pixel = Actor('pixels')
pixel.pos = (100,300)
shrubs_images = ['shrub', 'shrub2' , 'shrub3']
shrubs_list = []
life = 3
game_over = False
score = 0


def draw():
    global game_over

    if game_over == True:
        return
    screen.blit('plainbg',(0,0))
    pixel.draw()
    for shrub in shrubs_list:
        shrub.draw()

    screen.draw.text('life ='+ str(life),(10 , 10))
    screen.draw.text('score = '+ str(score),(10,20))

def on_key_down(key):
    if key == keys.SPACE and pixel.y >= 300:
        for i in range(20):
            pixel.y -= 9

def update():
    global life
    global game_over
    global score

    if game_over == True:
        return
    if pixel.y < 300:
        pixel.y += 3

    for shrub in shrubs_list:
        shrub.x -= 10

        if shrub.colliderect(pixel):
            life = life - 1
            shrubs_list.remove(shrub)

        if shrub.x <= 0:
            score = score + 1
            shrubs_list.remove(shrub)


    if life == 0:
        game_over = True





def hurdles():
    shrubs = Actor(random.choice(shrubs_images))
    shrubs.pos = (700,300)
    shrubs_list.append(shrubs)
    clock.schedule(hurdles,random.randint(1,5))



    
    

hurdles()



pgzrun.go()
