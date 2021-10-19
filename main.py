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
playerX = 390
playerY = 480

def player():
    screen.blit(playerimg,(playerX, playerY))

#The main Game Loop

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill((129,129,150))
    player()
    pygame.display.update()
    







