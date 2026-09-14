import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

font1 = pygame.font.SysFont('Arial', 30)

mercedes = pygame.image.load('images/mercedes.png')
nike = pygame.image.load('images/nike.png')
google = pygame.image.load('images/google.png')
adidas = pygame.image.load('images/adidas.png')
microsoft = pygame.image.load('images/microsoft.png')
audi = pygame.image.load('images/audi.png')

screen.fill('white')

while True:
    screen.blit(mercedes, (650, 75))
    screen.blit(nike, (650, 150))
    screen.blit(microsoft, (650, 225))
    screen.blit(audi, (650, 300))
    screen.blit(google, (650, 375))
    screen.blit(adidas, (650, 450))
    text = font1.render('Nike', True, (0, 0, 0))
    screen.blit(text, (50, 450))

    text = font1.render('Mercedes', True, (0, 0, 0))
    screen.blit(text, (50, 375))

    text = font1.render('Microsoft', True, (0, 0, 0))
    screen.blit(text, (50, 225))

    text = font1.render('Audi', True, (0, 0, 0))
    screen.blit(text, (50, 150))

    text = font1.render('Google', True, (0, 0, 0))
    screen.blit(text, (50, 300))

    text = font1.render('Adidas', True, (0, 0, 0))
    screen.blit(text, (50, 75))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen,('black'),pos,pos2,5)
            pygame.display.update()


        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

    
