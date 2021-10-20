import pygame

#initialization
pygame.init()

#screen
screen = pygame.display.set_mode((1000,800))

running = True

#Title

pygame.display.set_caption('The Harsh Game')

# Background
back = pygame.image.load('background.jpg')

#Icon

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player

playerimg = pygame.image.load('player.png')
playerX = 480
playerY = 720
xchange = 0
ychange = 0

#Enemy

enemyimg = pygame.image.load('enemy1.png')
enemyxchange = 0.3
enemyychange = 0.1

#Bullet

bulleticon = pygame.image.load('bullet.png')
bulletX = 480
bulletY = playerY
bulletxchange = 0
bulletychange = 3
bulletstate = 'ready'
b=1

def player(x, y):
    screen.blit(playerimg,(x, y))

def enemy(x,y):
    screen.blit(enemyimg, (x,y))

def fire_bullet(x,y):
    global bulletstate
    bulletstate = 'fire'
    screen.blit(bulleticon, (x+16,y+20))

# Enemy Randomizer

from math import pi

import VQErandom
enemyX = VQErandom.VarQRandom(0, 960, pi/4, 1, 4)
enemyY = VQErandom.VarQRandom(0, 300, 0, 1, 4)

#The main Game Loop

while running:

    screen.fill((129,129,150))
    screen.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -0.5
            if event.key == pygame.K_RIGHT:
                xchange = 0.5
            if event.key == pygame.K_UP:
                ychange = -0.5
            if event.key == pygame.K_DOWN:
                ychange = 0.5
            if event.key == pygame.K_SPACE:
                if bulletstate=='ready':
                    bulletX = playerX
                    fire_bullet(bulletX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                xchange = 0
            if event.key == pygame.K_RIGHT:
                xchange = 0      
            if event.key == pygame.K_UP:
                ychange = 0
            if event.key == pygame.K_DOWN:
                ychange = 0          
    
    playerX += xchange
    playerY += ychange

    if playerX<0:
        playerX = 0
    elif playerX>932:
        playerX=932
    if playerY<0:
        playerY=0
    elif playerY>734:
        playerY=734

    enemyX += enemyxchange

    if enemyX<=0:
        enemyxchange=0.4

    elif enemyX>=870:
        enemyxchange=-0.4
    
    if enemyX<=10:
        enemyY +=0.4
    elif enemyX>=950:
        enemyY +=0.4
    
    player(playerX, playerY)

    enemy(enemyX, enemyY)
    if bulletY<=0:
        bulletY = playerY
        bulletstate='ready'

    if bulletstate is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletychange

    pygame.display.update()


    







