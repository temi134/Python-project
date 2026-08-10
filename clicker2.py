import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))

sadface = pygame.image.load("images/sadface.png")
happyface = pygame.image.load("images/happyface.png")

is_happy = True

points = 0
lives = 3

font = pygame.font.SysFont(None, 36)

game_over = False
win = False

last_face_change = pygame.time.get_ticks()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not win:

            face_rect = happyface.get_rect(topleft=(10, 10))

            if face_rect.collidepoint(event.pos):

                if is_happy:
                    points += 1
                else:
                    lives -= 1

                if points >= 30:
                    win = True

                if lives <= 0:
                    game_over = True

    current_time = pygame.time.get_ticks()

    if current_time - last_face_change >= 2000 and not game_over and not win:

        face_change = random.choice([True, False])

        if face_change:
            is_happy = not is_happy

        last_face_change = current_time

    screen.fill("white")

    if is_happy:
        screen.blit(happyface, (10, 10))
    else:
        screen.blit(sadface, (10, 10))

    points_text = font.render("Points: " + str(points), True, "black")
    screen.blit(points_text, (10, 300))

    lives_text = font.render("Lives: " + str(lives), True, "black")
    screen.blit(lives_text, (10, 340))

    if win:
        win_text = font.render("YOU WIN!", True, "green")
        screen.blit(win_text, (130, 180))

    if game_over:
        lose_text = font.render("YOU LOSE!", True, "red")
        screen.blit(lose_text, (125, 180))

    pygame.display.update()