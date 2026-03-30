import random

WIDTH = 800
HEIGHT = 600

player = Actor("pixel")
player.x = 50
player.y = HEIGHT // 2

enemy = Actor("enemy")
enemy.x = WIDTH - 50
enemy.y = HEIGHT // 2

bullets = []
snowballs = []

score = 0
lives = 3

enemy_direction = 3

def draw():
    screen.clear()
    screen.fill((0, 0, 50))

    player.draw()
    enemy.draw()

    for bullet in bullets:
        bullet.draw()

    for snowball in snowballs:
        snowball.draw()

    screen.draw.text("Score: " + str(score), (10, 10), color="white")
    screen.draw.text("Lives: " + str(lives), (10, 40), color="white")


def update():
    global lives, score, enemy_direction

    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    if player.y < 0:
        player.y = 0
    if player.y > HEIGHT:
        player.y = HEIGHT

    enemy.y += enemy_direction
    if enemy.y < 50 or enemy.y > HEIGHT - 50:
        enemy_direction *= -1

    i = 0
    while i < len(bullets):
        bullets[i].x += 7
        if bullets[i].x > WIDTH:
            bullets.pop(i)
        else:
            i += 1

    i = 0
    while i < len(snowballs):
        snowballs[i].x -= 5
        if snowballs[i].x < 0:
            snowballs.pop(i)
            lives -= 1
        else:
            i += 1

    i = 0
    while i < len(bullets):
        j = 0
        hit = False
        while j < len(snowballs):
            if bullets[i].colliderect(snowballs[j]):
                bullets.pop(i)
                snowballs.pop(j)
                score += 1
                hit = True
                break
            else:
                j += 1
        if not hit:
            i += 1

    i = 0
    while i < len(snowballs):
        if snowballs[i].colliderect(player):
            snowballs.pop(i)
            lives -= 1
        else:
            i += 1

    if lives <= 0:
        exit()


def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = player.x + 20
        bullet.y = player.y
        bullets.append(bullet)


def spawn_snowball():
    snowball = Actor("snowball")
    snowball.x = enemy.x - 20
    snowball.y = enemy.y
    snowballs.append(snowball)


clock.schedule_interval(spawn_snowball, 1.5)