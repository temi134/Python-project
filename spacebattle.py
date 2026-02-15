import pgzrun
import random

WIDTH = 612
HEIGHT = 445

player = Actor("player")
player.pos = (WIDTH // 2, HEIGHT - 50)

enemies = []
bullets = []
red_bullets = []
life = 3
score = 0

def create_enemies():
    for row in range(2):
        for col in range(6):
            enemy = Actor("enemy")
            enemy.x = 80 + col * 80
            enemy.y = 60 + row * 60
            enemies.append(enemy)



def draw():
    screen.blit("spacebg", (0, 0))
    player.draw()

    for enemy in enemies:
        enemy.draw()

    for bullet in bullets:
        bullet.draw()

    for red_bullet in red_bullets:
        red_bullet.draw()

    screen.draw.text('score'+str(score),(10,50))
    screen.draw.text('lives'+str(life),(500,50))
    




def update():
    global life
    global score

    # Move player
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

    # Move bullets
    for bullet in bullets:
        bullet.y -= 5

        # Check collision
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score = score + 1
                break
            if bullet.y < 0 and bullet in bullets:
                bullets.remove(bullet)
                

        

    for red_bullet in red_bullets:
        red_bullet.y += 3
        if red_bullet.colliderect(player):
            life=life-1
            red_bullets.remove(red_bullet)
        if life == 0:
            pass
        if red_bullet.y > 445:
            red_bullets.remove(red_bullet)


def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("player_bullet")
        bullet.pos = (player.x, player.y - 20)
        bullets.append(bullet)

def enemy_bullet():
    if enemies:
        shooter = random.choice(enemies)
        red_bullet = Actor('red_bullet')
        red_bullet.pos = shooter.pos
        red_bullets.append(red_bullet)
        clock.schedule(enemy_bullet,1)






create_enemies()
enemy_bullet()
    
    
pgzrun.go()
