import pygame

#initialization
pygame.init()

#screen
screen = pygame.display.set_mode((1000,800))

running = True

#Title

pygame.display.set_caption('A Bad Space Game')

# Background
back = pygame.image.load('background.jpg')

#Icon

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Enemy Randomizer

from math import pi, sqrt

import VQErandom


#Player

playerimg = pygame.image.load('player.png')
playerX = 480
playerY = 720
xchange = 0
ychange = 0

#Enemy
enemyimg = []
enemyX= []
enemyY= []
enemyxchange = []
enemyychange = 0.6
for i in range (3):
    enemyimg.append(pygame.image.load('enemy1.png'))
    enemyX.append(100 * (VQErandom.VarQRandom(0, 9.6, 0, 1, 4)))
    enemyY.append(100 * (VQErandom.VarQRandom(0, 3, 0, 1, 4)))
    enemyxchange.append(0.8)

#Bullet

bulleticon = pygame.image.load('bullet.png')
bulletX = 480
bulletY = playerY
bulletxchange = 0
bulletychange = 3
bulletstate = 'ready'
b=1

#Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scorex = 10
scorey= 10

def show_score(x,y):
    scoreshow = font.render('Score:'+str(score_value), True, (255,255,255))
    screen.blit(scoreshow, (x, y))

def player(x, y):
    screen.blit(playerimg,(x, y))

def enemy(k,x,y):
    screen.blit(enemyimg[k],(x,y))

def fire_bullet(x,y):
    global bulletstate
    bulletstate = 'fire'
    screen.blit(bulleticon, (x+16,y+20))

#The main Game Loop

def collision(x1, y1, x2, y2):
    distance = sqrt((x2-x1)**2+(y2-y1)**2)
    if distance<30:
        return True
    else:
        return False

# Game over
over_font = pygame.font.Font('freesansbold.ttf', 64)
overx = 10
overy= 10
def game_over(x,y):
    scoreshow = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(scoreshow, (x, y))


while running:

    screen.fill((129,129,150))
    screen.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -0.9
            if event.key == pygame.K_RIGHT:
                xchange = 0.9
            if event.key == pygame.K_UP:
                ychange = -0.9
            if event.key == pygame.K_DOWN:
                ychange = 0.9
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

    for i in range (3):
        #Over

        if enemyY[i]>650:
            for j in range (3):
                enemyY[j]=2000
            game_over(400, 300)
            break

        #Over
        checkene = collision(enemyX[i], enemyY[i], playerX, playerY)

        if checkene:
            for j in range (3):
                enemyY[j]=2000
            game_over(0, 300)
            break        

        enemyX[i] += enemyxchange[i]

        if enemyX[i]<=0:
            enemyxchange[i]=0.8

        elif enemyX[i]>=870:
            enemyxchange[i]=-0.8
        
        if enemyX[i]<=30:
            enemyY[i] +=0.8

        elif enemyX[i]>=800:
            enemyY[i] +=0.8

        enemy(i, enemyX[i], enemyY[i])


        
    player(playerX, playerY)

    if bulletY<=0:
        bulletY = playerY
        bulletstate='ready'

    if bulletstate is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletychange

    #Collision
    for i in range (3):
        checkcol = collision(enemyX[i], enemyY[i], bulletX, bulletY)

        if checkcol:
            bulletY = playerY
            bulletstate='ready'
            score_value = score_value +1
            enemyX[i] = 100 * (VQErandom.VarQRandom(0, 9.6, 0, 1, 4))
            enemyY[i] = 100 * (VQErandom.VarQRandom(0, 3, 0, 1, 4))

        show_score(scorex, scorey) 


    pygame.display.update()


    







