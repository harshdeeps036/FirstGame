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

def player(x, y):
    screen.blit(playerimg,(x, y))

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
    player(playerX, playerY)

    pygame.display.update()


    







