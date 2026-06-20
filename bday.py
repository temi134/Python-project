import pygame

pygame.init()

screen = pygame.display.set_mode((750,525))

bday = pygame.image.load('images/birthday.jpg')

font1 = pygame.font.SysFont('Arial',60)
font2 = pygame.font.SysFont('Arial',30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    text = font1.render('Happy Birthday',True,(0,0,0))
    text2 = font2.render('Have a good day',True,(0,0,0))
    screen.blit(bday,(0,0))
    screen.blit(text,(220,250))
    screen.blit(text2,(250,325))
    pygame.display.update()

    