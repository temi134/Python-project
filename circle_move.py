import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))


class Circle():
    def __init__(self, colour, position, radius, width):
        self.colour = colour
        self.position = list(position)  
        self.radius = radius
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.position,self.radius,self.width)

    def move_right(self, amount):
        self.position[0] += amount


circle1 = Circle('white', (200, 200), 10, 0)

while True:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            circle1.move_right(-20)

    circle1.draw()

    pygame.display.update()