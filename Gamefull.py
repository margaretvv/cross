import pygame
import random
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.font.init() 
font1 = pygame.font.Font(None, 80) 
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
BLACK = (0,0,0)
player = pygame.Rect(screen.get_width()/2 - 25,600,50,50)

block1_width = random.randint(50,1210)
block1_height = 50
block1 = pygame.Rect(0,0,block1_width,block1_height)

block2 = pygame.Rect(70 + block1.width,0,1280 - 70 - block1_width,block1_height)
while running:
    
    if block1.y >= 720:
        block1.y = 0
        block2.y = 0
        block1.width = random.randint(50,1210)
        block2.x = block1.width + 70
        block2.width = 1280 - 70 - block1.width
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.x += 8
    if keys[pygame.K_LEFT]:
        player.x -= 8
   

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lime")
    
    # RENDER YOUR GAME HERE
    block1.y += 3
    block2.y += 3
    pygame.draw.rect(screen,BLACK,player)

    pygame.draw.rect(screen,BLACK,block1)

    pygame.draw.rect(screen,BLACK,block2)
    if pygame.Rect.colliderect(player,block1) or pygame.Rect.colliderect(player,block2):
        screen.blit(lose,(500, 500))
        pygame.display.flip()
        sleep(5)
        running=False
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()