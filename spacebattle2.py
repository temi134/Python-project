import pygame
pygame.init()

screen = pygame.display.set_mode((800,560))

spacebg = pygame.image.load('images/spacebg.jpg')

class Spacecraft(pygame.sprite.Sprite):
    def __init__(self , x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    


    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.rect.x += 1

        if key[pygame.K_LEFT]:
            self.rect.x -= 1

space1 = Spacecraft(400,400)

sprite_group = pygame.sprite.Group()
sprite_group.add(space1)

class Spacecraft2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/player2.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_d]:
                self.rect.x += 1

        if key[pygame.K_a]:
                self.rect.x -= 1

space2 = Spacecraft2(400,140)
sprite_group2 = pygame.sprite.Group()
sprite_group2.add(space2)



    


while True:
    screen.blit(spacebg,(0,0))
    sprite_group.draw(screen)
    sprite_group.update()
    sprite_group2.draw(screen)
    sprite_group2.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()


        