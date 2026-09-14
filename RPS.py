import pygame
import random

screen = pygame.display.set_mode((400,400))
housebg = pygame.image.load('images/house')
housebg = pygame.transform.scale(housebg,(400,400))

rock = pygame.image.load('images/rock.png')
scissors = pygame.image.load('images/scissors.png')
paper = pygame.image.load('images/paper.png')

rock_rect = rock.get_rect(center = (75,300))
scissors_rect = scissors.get_rect(center = (215,300))
paper_rect = scissors.get_rect(center = (355,300))

choice = random.choice(['rock','paper','scissors'])
users_choice = ''

while True:
    screen.blit(housebg,(0,0))
    screen.blit(rock,rock_rect)
    screen.blit(scissors,scissors_rect)
    screen.blit(paper,paper_rect)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock.rect.collidepoint(pygame.mouse.get_pos()):
                users_choice = 'rock'

            if paper.rect.collidepoint(pygame.mouse.get_pos()):
                users_choice = 'paper'

            if scissors.rect.collidepoint(pygame.mouse.get_pos()):
                users_choice = 'scissors'
                
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()