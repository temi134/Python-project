import pgzrun
import random

WIDTH = 612
HEIGHT = 445

player = Actor("player")
player2 = Actor('player2')
player.pos = (WIDTH - 200, HEIGHT - 50)
player2.pos = (WIDTH //3, HEIGHT - 50)

enemies = []
bullets = []
hearts = []
red_bullets = []

life_1 = 20
life_2 = 20
score = 0

boss = None
boss_life = 20
boss_active = False
game_over = False


def create_enemies():
    for row in range(2):
        for col in range(6):
            enemy = Actor("enemy")
            enemy.x = 80 + col * 80
            enemy.y = 60 + row * 60
            enemies.append(enemy)
    clock.schedule(create_enemies, 6)


def heal():
    heart = Actor("heart")
    heart.x = random.randint(20, WIDTH - 20)
    heart.y = 0
    hearts.append(heart)
    clock.schedule(heal, 30)


def draw():
    screen.blit("spacebg", (0, 0))

    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        return

    player.draw()
    player2.draw()

    for enemy in enemies:
        enemy.draw()

    for bullet in bullets:
        bullet.draw()

    for red_bullet in red_bullets:
        red_bullet.draw()

    for heart in hearts:
        heart.draw()

    if boss_active and boss:
        boss.draw()
        screen.draw.text("Boss HP: " + str(boss_life), (250, 20))

    screen.draw.text("Score: " + str(score), (10, 50))
    screen.draw.text("player 1 lives: " + str(life_1), (450,400))
    screen.draw.text('player 2 lives:' + str(life_2),(1,400))


def update():
    global game_over, life_1, score, life_2
    global boss, boss_active, boss_life

    if game_over:
        return

    if life_1 <= 0 or life_2 <= 0:
        game_over = True
        return

    if score > 0 and score % 40 == 0 and not boss_active:
        boss = Actor("boss")
        boss.pos = (WIDTH // 2, 80)
        boss_active = True
        boss_life = 20
        boss_shoot()

    if keyboard.left and player.left > 0:
        player.x -= 5
    if keyboard.right and player.right < WIDTH:
        player.x += 5

    if keyboard.a and player2.left > 0:
        player2.x -= 5
    if keyboard.d and player2.right < WIDTH:
        player2.x += 5

    for enemy in enemies:
        enemy.y += 0.3

        if enemy.colliderect(player):
            life_1 -= 5
            enemies.remove(enemy)

        elif enemy.colliderect(player2):
            life_2 -= 5
            enemies.remove(enemy)

    for bullet in bullets:
        bullet.y -= 5

        if bullet.y < 0:
            bullets.remove(bullet)
            continue

        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                score += 1
                break

        if boss_active and boss and bullet in bullets:
            if bullet.colliderect(boss):
                boss_life -= 1
                bullets.remove(bullet)

                if boss_life <= 0:
                    boss_active = False
                    boss = None
                    score += 10

    if boss_active and boss:
        boss.x += random.randint(-3, 3)
        boss.y += random.randint(-1, 1)

        boss.x = max(0, min(WIDTH, boss.x))
        boss.y = max(0, min(150, boss.y))

    for red_bullet in red_bullets:
        red_bullet.y += 5

        if red_bullet.colliderect(player):
            life_1 -= 1
            red_bullets.remove(red_bullet)

        elif red_bullet.colliderect(player2):
            life_2 -= 1
            red_bullets.remove(red_bullet)

        elif red_bullet.y > HEIGHT:
            red_bullets.remove(red_bullet)

    for heart in hearts:
        heart.y += 2

        if heart.colliderect(player):
            life_1 += 5
            hearts.remove(heart)

        elif heart.colliderect(player2):
            life_2 += 5
            hearts.remove(heart)

        elif heart.y > HEIGHT:
            hearts.remove(heart)


def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("player_bullet")
        bullet.pos = (player.x, player.y - 20)
        bullets.append(bullet)

    if key == keys.W:
        bullet = Actor('player_bullet')
        bullet.pos = (player2.x, player2.y - 20)
        bullets.append(bullet)


def enemy_bullet():
    if enemies:
        shooter = random.choice(enemies)
        red_bullet = Actor("red_bullet")
        red_bullet.pos = shooter.pos
        red_bullets.append(red_bullet)

    clock.schedule(enemy_bullet, 1)


def boss_shoot():
    if boss_active and boss:
        red_bullet = Actor("red_bullet")
        red_bullet.pos = boss.pos
        red_bullets.append(red_bullet)
        clock.schedule(boss_shoot, 0.7)


create_enemies()
enemy_bullet()
clock.schedule(heal,30)

pgzrun.go()