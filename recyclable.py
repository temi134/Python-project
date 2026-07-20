import pygame
import random

pygame.init()

screen = pygame.display.set_mode((750, 750))

class Recyclable(pygame.sprite.Sprite):
    def __init__(self, x, y,images):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(images)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.screen = screen

class Non_Recyclable(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/non_recyclable.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.screen = screen

images = ["images/recyclable.png" , "images/can.jpg"]

recyclable_group = pygame.sprite.Group()
for i in range(25):
    x = random.randint(50, 730)
    y = random.randint(50, 730)
    image = random.choice(images)
    recyclable1 = Recyclable(x, y ,image )
    recyclable_group.add(recyclable1)

non_recyclable_group = pygame.sprite.Group()
for i in range(10):
    x = random.randint(50, 730)
    y = random.randint(50, 730)
    non_recyclable1 = Non_Recyclable(x,y)
    non_recyclable_group.add(non_recyclable1)

while True:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    recyclable_group.draw(screen)
    non_recyclable_group.draw(screen)
    pygame.display.update()

