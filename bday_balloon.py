import pygame

pygame.init()

screen = pygame.display.set_mode((750,750))

bday = pygame.image.load('images/birthday2.jpg')

font1 = pygame.font.SysFont('Arial',60)

class Balloon():
    def __init__(self,x,y):
        self.image = pygame.image.load('images/balloon.png')
        self.x = x
        self.y = y
        self.screen = screen

    def update(self):
        balloon1.y = balloon1.y - 1

balloon1 = Balloon(500,600)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if balloon1.y > 0:
            balloon1.update()
    screen.blit(bday,(0,0))
    text = font1.render('Happy Birthday',True,(0,0,0))
    screen.blit(text,(375,375))
    screen.blit(balloon1.image,(balloon1.x,balloon1.y))

    pygame.display.update()
