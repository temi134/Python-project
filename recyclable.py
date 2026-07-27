import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,560))
background = pygame.image.load("images/nature.jpg")
score = 0
lives = 3
font = pygame.font.SysFont("Arial",20,"bold")
font1 = pygame.font.SysFont("Arial",100,"bold")
class Recyclable(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(images)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.screen = screen

class Non_Recyclable(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/non_recyclable.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.screen = screen

class Bin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bin.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.screen = screen


    def update(self):
        global score , lives
        
        key = pygame.key.get_pressed()
        if pygame.sprite.spritecollide(self, recyclable_group,True):
            score = score + 1
        if pygame.sprite.spritecollide(self, non_recyclable_group,True):
            lives = lives - 1
            
    

        if key[pygame.K_RIGHT]:
            self.rect.x += 1

        if key[pygame.K_LEFT]:
            self.rect.x -= 1

        if key[pygame.K_UP]:
            self.rect.y -= 1

        if key[pygame.K_DOWN]:
            self.rect.y += 1

images = ["images/recyclable.png", "images/can.png"]

recyclable_group = pygame.sprite.Group()
for i in range(25):
    x = random.randint(100, 730)
    y = random.randint(100, 510)
    image = random.choice(images)
    recyclable1 = Recyclable(x, y, image)
    recyclable_group.add(recyclable1)

non_recyclable_group = pygame.sprite.Group()
for i in range(10):
    x = random.randint(100, 730)
    y = random.randint(100, 510)
    non_recyclable1 = Non_Recyclable(x, y)
    non_recyclable_group.add(non_recyclable1)
print(len(recyclable_group))
bin1 = Bin(50, 50)

while True:
    screen.blit(background,(0,0))
    text = font.render("score = "+str (score),True,"black")
    text2 = font.render("lives ="+str(lives),True,"black")
    text3 = font1.render("you won",True,"black")
    text4 = font1.render("you lost",True,"black")
    screen.blit(text, (10,10))
    screen.blit(text2,(10,40))
    if score == 25:
        screen.blit(text3,(350,250))
        pygame.display.update()
        time.sleep(3)
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if lives <= 0:
        screen.blit(text4,(350,250))
        pygame.display.update()
        time.sleep(3)
        break

    recyclable_group.draw(screen)
    non_recyclable_group.draw(screen)

    bin1.update()
    screen.blit(bin1.image, bin1.rect)
    

    pygame.display.update()

