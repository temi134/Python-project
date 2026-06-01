import pygame

pygame.init()

screen = pygame.display.set_mode(([500,500]))



class Circle():
    def __init__(self , colour , position , radius , width):
        self.colour = colour
        self.position = position 
        self.radius = radius
        self.width = width
        self.screen = screen

    def draw(self):
            pygame.draw.circle(self.screen , self.colour , self.position , self.radius , self.width)

    def grow(self , size):
         self.radius = self.radius + size
         self.draw()

    def shrink(self, size):
         self.radius = self.radius - size
         self.draw()
         

circle1 = Circle('white' , (200,200) , 10 , 0)
circle2 = Circle('white', (400,200) , 100 , 0)

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
             circle1.grow(2)
             circle2.shrink(5)
             pygame.display.update()
    circle1.draw()
    circle2.draw()
    pygame.display.update()

    