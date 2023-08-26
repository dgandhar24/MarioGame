import pygame
from Constants import *



pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('GD Mario')
clock = pygame.time.Clock()

playerImg = pygame.image.load("player.png")
platformImg = pygame.image.load("level_1.png")

def player(y):
    gameDisplay.blit(playerImg,(392,y))

def platform(x):
    gameDisplay.blit(platformImg,(x,0))

def game_loop():
    x = 0
    y = 100

    x_change = 0
    y_change = 0

    c = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = 7
                elif event.key == pygame.K_RIGHT:
                    x_change = -7
                if event.key == pygame.K_UP:
                    if c <= 5:
                        y_change = -5
                        c += 1
                    else:
                        y_change = 0
                #elif event.key == pygame.K_DOWN:
                 #   y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP:
                    if c > 0:
                        y_change = 5
                        c -= 1
                    else:
                        y_change = 0

        x += x_change
        y += y_change
        if x < -8284:
            x = -8284
        if x > 0:
            x = 0
        if y < 0:
            y = 0
        if y > 600:
            y = 590

        platform(x)
        player(y)

        pygame.display.update();
        clock.tick(120)

game_loop()
pygame.quit()
quit()
