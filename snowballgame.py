import pgzrun
import random

WIDTH = 800
HEIGHT = 500

player = Actor('bunny')
player.pos = (50 , HEIGHT // 2)

enemy = Actor('yeti')
enemy.pos = (WIDTH - 50, HEIGHT // 2)

speed = 3
snowball_list = []

def draw():
    screen.blit('snowbg', (0,0))
    player.draw()
    enemy.draw()
    for snowball in snowball_list:
        snowball.draw()


def update():
    global speed 

    if keyboard.up and player.y > 0:
        player.y -= 5
    if keyboard.down and player.y < 500:
        player.y += 5

    enemy.y = enemy.y + speed
    if enemy.y >= 500:
        speed = -3
    if enemy.y <= 0:
        speed = 3

    for snowball in snowball_list:
        snowball.x = snowball.x - 5

def enemy_snowball():
    snowball = Actor('snowball')
    snowball.y = enemy.y
    snowball.x = enemy.x
    snowball_list.append(snowball)
    clock.schedule(enemy_snowball, random.randint(1,2))


enemy_snowball()
    

pgzrun.go()