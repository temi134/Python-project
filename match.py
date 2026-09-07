import pygame

screen = pygame.display.set_mode((800,800))


mercedes = pygame.image.load('images/mercedes.png')
nike = pygame.image.load('images/nike.png')
google = pygame.image.load('images/google.png')
adidas = pygame.image.load('images/adidas.png')
microsoft = pygame.image.load('images/microsoft.png')
audi = pygame.image.load('images/audi.png')

while True:
    screen.fill('white')
    screen.blit(mercedes,(650,75))
    screen.blit(nike,(650,150))
    screen.blit(microsoft,(650,225))
    screen.blit(audi,(650,300))
    screen.blit(google,(650,375))
    screen.blit(adidas,(650,450))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    
