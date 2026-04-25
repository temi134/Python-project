import pgzrun
import random

WIDTH = 300
HEIGHT = 400

player = Actor('player')
player.pos = (150, 350)

tiles = []
game_over = False
positions = [50, 150, 250]
score = 0

def draw():

    if game_over:
        screen.fill("black")

        screen.draw.text("GAME OVER", center=(150, 200), fontsize=40, color="white")
        return
       
    screen.fill("black")

    for tile in tiles:
        tile.draw()

    player.draw()
    screen.draw.text('score ='+ str(score) ,(50, 10), color = 'white')

    


def update():
    global game_over
    global score
    global redrect
    if game_over:
        return

    if keyboard.left:
        player.x -= 9
    if keyboard.right:
        player.x += 9

    player.x = max(0, min(player.x, WIDTH))

    for tile in tiles:
        tile.y += 4

        if tile.colliderect(player):
            if tile.image == "redrect":
                game_over = True

    for tile in tiles:
        if tile.y > HEIGHT:
            if tile.image == 'redrect':
                score = score + 1
            tiles.remove(tile)
            

        


def spawn_tiles():
    y = -50

    if random.choice([True, False]):
        types = ["redrect", "redrect", "whiterect"]
    else:
        types = ["whiterect", "whiterect", "redrect"]

    random.shuffle(types)

    for i in range(3):
        tile = Actor(types[i])
        tile.pos = (positions[i], y)
        tiles.append(tile)
    clock.schedule(spawn_tiles,1)

spawn_tiles()

pgzrun.go()