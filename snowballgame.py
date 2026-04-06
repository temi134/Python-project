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
arrow_list = []
bigsnowball_list = []
arrow2_list = []
heart_list = []

game_over = False
score = 0
lives = 5


def draw():
    if game_over == True:
        screen.blit('gameover',(0,0))
        return

    screen.blit('snowbg', (0,0))
    player.draw()
    enemy.draw()

    for snowball in snowball_list:
        snowball.draw()

    for arrow in arrow_list:
        arrow.draw()

    for bigsnowball in bigsnowball_list:
        bigsnowball.draw()

    for arrow2 in arrow2_list:
        arrow2.draw()

    for heart in heart_list:
        heart.draw()

    screen.draw.text("Score: " + str(score), (10, 50))
    screen.draw.text("Lives: " + str(lives), (10, 70))


def update():
    global speed, score, lives, game_over , heart

    if lives == 0 and game_over == False:
        game_over = True

    if keyboard.up and player.y > 0:
        player.y -= 5
    if keyboard.down and player.y < HEIGHT:
        player.y += 5

    enemy.y += speed
    if enemy.y >= HEIGHT:
        speed = -3
    if enemy.y <= 0:
        speed = 3

    for snowball in snowball_list:
        snowball.x -= 5

        if snowball.x < 0:
            snowball_list.remove(snowball)
            lives -= 1

        elif snowball.colliderect(player):
            snowball_list.remove(snowball)
            lives -= 1

    for arrow in arrow_list:
        arrow.x += 7

        if arrow.x > WIDTH:
            arrow_list.remove(arrow)

    for arrow2 in arrow2_list:
        arrow2.x += 7

    for heart in heart_list:
        heart.x -= 5

        if heart.x < 0:
            heart_list.remove(heart)

        elif heart.colliderect(player):
            heart_list.remove(heart)
            lives = min(lives + 1, 5)

    for bigsnowball in bigsnowball_list:
        bigsnowball.x -= 5

        if bigsnowball.x < 0:
            heart_list.remove(heart)

        elif bigsnowball.colliderect(player):
            heart_list.remove(heart)
            lives = lives - 3

  

    for arrow in arrow_list:
        for snowball in snowball_list:
            if arrow.colliderect(snowball):
                arrow_list.remove(arrow)
                snowball_list.remove(snowball)
                score += 1
                break

    for arrow2 in arrow2_list:
        for bigsnowball in bigsnowball_list:
            if arrow2.colliderect(bigsnowball):
                arrow2_list.remove(arrow2)
                bigsnowball_list.remove(bigsnowball)


def on_key_down(key):
    if key == keys.SPACE:
        shoot_arrow()
    if key == keys.RIGHT:
        arrow2s()


def shoot_arrow():
    arrow = Actor('arrow')
    arrow.pos = (player.x + 20, player.y)
    arrow_list.append(arrow)


def arrow2s():
    arrow2 = Actor('arrow2')
    arrow2.pos = (player.x + 20 ,player.y)
    arrow2_list.append(arrow2)


def enemy_snowball():
    snowball = Actor('snowball')
    snowball.pos = (enemy.x - 20, enemy.y)
    snowball_list.append(snowball)
    clock.schedule(enemy_snowball, random.uniform(1,2))


def bigsnowballs():
    bigsnowball = Actor('bigsnowball')
    bigsnowball.pos = (enemy.x - 20 , enemy.y)
    bigsnowball_list.append(bigsnowball)
    clock.schedule(bigsnowballs, 5)


def spawn_heart():
    heart = Actor('heart')
    heart.pos = (enemy.x - 20, random.randint(20, HEIGHT - 20))
    heart_list.append(heart)
    clock.schedule(spawn_heart, random.uniform(20 , 30))


enemy_snowball()
clock.schedule(bigsnowballs, 10)
clock.schedule(spawn_heart, 20)

pgzrun.go()
    