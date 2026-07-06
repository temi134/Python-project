import pygame

pygame.init()

screen = pygame.display.set_mode((250,250))

sadface = pygame.image.load("images/sadface.png")
happyface = pygame.image.load("images/happyface.png")

face = sadface

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            face = happyface

        if event.type == pygame.MOUSEBUTTONUP:
            face = sadface

    screen.fill("white")
    screen.blit(face, (10,10))

    pygame.display.update()

