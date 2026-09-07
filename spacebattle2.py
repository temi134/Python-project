import pygame
import time
pygame.init()

screen = pygame.display.set_mode((800,560))

spacebg = pygame.image.load('images/spacebg.jpg')

font1 = pygame.font.SysFont('Arial',30) 
font2 = pygame.font.SysFont('Arial',100)

class Spacecraft(pygame.sprite.Sprite):
    def __init__(self , x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.last_shot = pygame.time.get_ticks()
        self.lives2 = 3
        

    


    def update(self):
        key = pygame.key.get_pressed()

        text = font1.render('lives:'+str(self.lives2),True,(255,255,255))  
        screen.blit(text,(720,50))


        if key[pygame.K_RIGHT]:
            self.rect.x += 1

        if key[pygame.K_LEFT]:
            self.rect.x -= 1

        current_time = pygame.time.get_ticks()

        if key[pygame.K_SPACE] and current_time - self.last_shot > 500:
            bullet1 = Bullet(self.rect.x + 35, self.rect.y)
            bullet_group1.add(bullet1)
            self.last_shot  = current_time

        if pygame.sprite.spritecollide(self,bullet_group2,True):
            self.lives2 -=  1



        

space1 = Spacecraft(400,500)

sprite_group = pygame.sprite.Group()
sprite_group.add(space1)

class Spacecraft2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/player2.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3

    def update(self):
        key = pygame.key.get_pressed()
        text2 = font1.render('lives:'+str(self.lives),True,(255,255,255))
        screen.blit(text2,(720,520))

        if key[pygame.K_d]:
                self.rect.x += 1

        if key[pygame.K_a]:
                self.rect.x -= 1

        if pygame.sprite.spritecollide(self,bullet_group1,True):
                self.lives -=  1

        current_time = pygame.time.get_ticks()

        if key[pygame.K_s] and current_time - self.last_shot > 500:
            bullet3 = Bullet2(self.rect.x + 50, self.rect.y)
            bullet_group2.add(bullet3)
            self.last_shot = current_time

        


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/player_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        self.rect.y -= 3

class Bullet2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/red_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        self.rect.y += 3
     

bullet_group1 = pygame.sprite.Group()
space2 = Spacecraft2(400,70)
sprite_group2 = pygame.sprite.Group()
sprite_group2.add(space2)
bullet_group2 = pygame.sprite.Group()

while True:
    screen.blit(spacebg,(0,0))
    sprite_group.draw(screen)
    sprite_group.update()
    sprite_group2.draw(screen)
    sprite_group2.update()
    bullet_group1.draw(screen)
    bullet_group1.update()
    bullet_group2.draw(screen)
    bullet_group2.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            

    if space2.lives <= 0:
         text3 = font2.render('Player2 wins',True,(255,255,255))
         screen.blit(text3,(150,200))
         pygame.display.update()
         time.sleep(3)
         pygame.quit()
    if space1.lives2 <= 0:
         text4 = font2.render('Player1 wins',True,(255,255,255))
         screen.blit(text4,(150,200))
         pygame.display.update()
         time.sleep(3)
         pygame.quit

    pygame.display.update()


        