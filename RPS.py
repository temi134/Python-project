import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400,400))

housebg = pygame.image.load('images/house.jpg')
housebg = pygame.transform.scale(housebg,(400,400))

font = pygame.font.Font(None,30)

rock = pygame.image.load('images/rock.png')
scissors = pygame.image.load('images/scissors.png')
paper = pygame.image.load('images/paper.png')

rock_rect = rock.get_rect(center = (75,150))
scissors_rect = scissors.get_rect(center = (215,150))
paper_rect = paper.get_rect(center = (355,150))

choice = random.choice(['rock','paper','scissors'])
users_choice = ''

start_time = 0


def winner():
    if users_choice == choice:
        return 'Draw!'

    if users_choice == 'rock' and choice == 'scissors':
        return 'You win!'

    if users_choice == 'paper' and choice == 'rock':
        return 'You win!'

    if users_choice == 'scissors' and choice == 'paper':
        return 'You win!'

    return 'Computer wins!'




while True:
    screen.blit(housebg,(0,0))

    screen.blit(rock,rock_rect)
    screen.blit(scissors,scissors_rect)
    screen.blit(paper,paper_rect)

    screen.blit(font.render('Rock', True, 'white'), (50,180))
    screen.blit(font.render('Scissors', True, 'white'), (180,180))
    screen.blit(font.render('Paper', True, 'white'), (335,180))

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN and users_choice == '':

            if rock_rect.collidepoint(event.pos):
                users_choice = 'rock'
                start_time = pygame.time.get_ticks()

            if paper_rect.collidepoint(event.pos):
                users_choice = 'paper'
                start_time = pygame.time.get_ticks()

            if scissors_rect.collidepoint(event.pos):
                users_choice = 'scissors'
                start_time = pygame.time.get_ticks()

        if event.type == pygame.QUIT:
            pygame.quit()

    if users_choice != '':
        text = font.render(winner(), True, 'white')
        screen.blit(text, (150,350))

        if pygame.time.get_ticks() - start_time >= 3000:
            users_choice = ''
            choice = random.choice(['rock','paper','scissors'])

    else:
        text = font.render('Choose another one!', True, 'white')
        screen.blit(text, (100,350))

    pygame.display.update()

pygame.quit()
