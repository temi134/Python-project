import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/bin.jpg')
        self.image = pygame.transform.scale(self.image,(90,110))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += 1

        if key[pygame.K_LEFT]:
            self.rect.x -= 1

        if key[pygame.K_UP]:
            self.rect.y -= 1

        if key[pygame.K_DOWN]:
            self.rect.y += 1

Bin1 = Bin(100,100)
group = pygame.sprite.Group()
group.add(Bin1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    group.draw(screen)
    group.update()
    pygame.display.update()







