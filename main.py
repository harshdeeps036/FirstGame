import pygame

#initialization
pygame.init()

#screen
screen = pygame.display.set_mode((800,600))

running = True

#Title

pygame.display.set_caption('The Harsh Game')

#Icon

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player

playerimg = pygame.image.load('player.png')
playerX = 380
playerY = 480
xchange = 0
ychange = 0

#Enemy

enemyimg = pygame.image.load('enemy1.png')
enemyX = 360
enemyY = 40
enemyxchange = 0
enemyychange = 0

def player(x, y):
    screen.blit(playerimg,(x, y))

def enemy(x,y):
    screen.blit(enemyimg, (x,y))

#The main Game Loop

while running:

    screen.fill((129,129,150))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -0.1
            if event.key == pygame.K_RIGHT:
                xchange = 0.1
            if event.key == pygame.K_UP:
                ychange = -0.1
            if event.key == pygame.K_DOWN:
                ychange = 0.1
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
    elif playerX>732:
        playerX=732
    if playerY<0:
        playerY=0
    elif playerY>534:
        playerY=534
    
    player(playerX, playerY)

    enemy(enemyX, enemyY)

    pygame.display.update()


    







