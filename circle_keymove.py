import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

screen.fill('white')

pygame.display.update()

class Circle():
    def __init__(self,colour,position,radius,width):
        self.colour = colour
        self.position = position
        self.radius = radius
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.position,self.radius,self.width)

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.position[0] += 1

        if key[pygame.K_LEFT]:
            self.position[0] -= 1

        if key[pygame.K_UP]:
            self.position[1] -= 1

        if key[pygame.K_DOWN]:
            self.position[1] += 1


circle1 = Circle('white', [300,250],10,0)

while True:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    circle1.draw()
    circle1.update()

    pygame.display.update()
