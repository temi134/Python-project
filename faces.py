import pygame
pygame.init()

screen = pygame.display.set_mode((250,250))

face = pygame.image.load('images/sadface.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            face = pygame.image.load('images/happyface.png')

        if event.type == pygame.MOUSEBUTTONUP:
            face = pygame.image.load('images/sadface.png')
    screen.fill('white')
    screen.blit(face,(10,10))
    pygame.display.update()

