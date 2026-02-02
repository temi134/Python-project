import pgzrun
import random

WIDTH = 600
HEIGHT = 508

jerry = Actor('jerry_image')      
cheese_list = []  
game_over = False


jerry.pos = (WIDTH // 2, HEIGHT - 50)

score = 0
fruit_speed = 4


def draw():
    if game_over:
        screen.blit('game_over',(0,0))
        return
    screen.blit('background2', (0, 0))
    screen.draw.text("Score: " + str(score), center=(50, 20), color="white")
    jerry.draw()
    for cheese in cheese_list:
        cheese.draw()


def reset_fruit():
    cheese = Actor('cheese')  
    cheese_list.append(cheese)
    cheese.y = 0
    cheese.x = random.randint(20, WIDTH - 20)
    clock.schedule(reset_fruit,random.randint(1,2))


def update():
    global score
    global game_over
    global fruit_speed

    if keyboard.right:
        jerry.x += 5
    if keyboard.left:
        jerry.x -= 5

    
    for cheese in cheese_list:
        cheese.y += fruit_speed

    
        if jerry.colliderect(cheese):
            score += 1
            cheese_list.remove(cheese)

        if cheese.y > HEIGHT:
            score -= 1
            cheese_list.remove(cheese)

    if score < 0:
        game_over = True
    elif score > 10:
        fruit_speed = 6



reset_fruit()
pgzrun.go()
