import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('Background_image.jpg')
background = pygame.transform.scale(background, (800, 600))

pygame.display.set_caption("Space Aliens")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

enemyimg = pygame.image.load('Enemy.png')
enemyx = random.randint (0, 736)
enemyy = random.randint (50, 150)
enemyx_change = 1
enemyy_change = 32

Playerimg = pygame.image.load('spaceship.png')
playerx = 370
playery = 500
playerx_change = 0

bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 8

global bullet_state  # Declare bullet_state as a global variable
bullet_state = "ready"  # Initialize bullet state

score = 0

def enemy (x,y):
    screen.blit (enemyimg, (x, y))

def Player (x,y):
    screen.blit (Playerimg, (x, y))

def fire_bullet (x,y):
    global bullet_state
    bullet_state = "fire"
    rotated_bullet = pygame.transform.rotate(bulletimg, 90)
    screen.blit (rotated_bullet, (x, y + 10))
    
def IsCollision (enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx-bulletx,2)  + math.pow(enemyy-bullety,2)))
    if distance < 27:
        return True
    else:
        return False


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -2
            if event.key == pygame.K_RIGHT:
                playerx_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Dynamically calculate the center of the player
                    player_center_x = playerx + (Playerimg.get_width() // 2) - (bulletimg.get_width() // 2)
                    bulletx = player_center_x
                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    screen.fill((0, 77, 255))
    screen.blit(background, (0, 0))


    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    if playerx >= 736:
        playerx = 736

    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 1
        enemyy += enemyy_change
    if enemyx >= 736:
        enemyx_change = -1
        enemyy += enemyy_change

    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change
        if bullety <= 0:
            bullety = 480
            bullet_state = "ready"
    
    collision = IsCollision(enemyx, enemyy, bulletx, bullety)
    if collision:
        bullety = 480
        bullet_state = "ready"
        score += 1
        print (score)
        enemyx = random.randint (0, 736)
        enemyy = random.randint (50, 150)

    enemy(enemyx, enemyy)
    Player(playerx, playery)

    pygame.display.update()