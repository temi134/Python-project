import pygame

pygame.init()

screen = pygame.display.set_mode((750,750))

bday = pygame.image.load('images/birthday2.jpg')

font1 = pygame.font.SysFont('Arial',60)

class Balloon():
    def __init__(self,x,y):
        self.image = 
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    text = font1.render('Happy Birthday',True,(0,0,0))
    screen.blit(text,(375,375))

