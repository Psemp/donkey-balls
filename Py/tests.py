import pygame
import math

pygame.init

win = pygame.display.set_mode ((750,750))

## Initial Position ##

#INCREMENT -->##

inc = 15

##Player##

plyrX = 50
plyrY = 50
plyrWDTH = 50 
plyrHGHT = 50
#vel = 5

##MEGA CHAD##

pnjX = 600
pnjY = 600
pnjWDTH = 50
pnjHGHT = 50
#vel = 5

run = True

while run == True:
    
    pygame.time.delay (100)

    ##EVENTS##
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False

    ## Keys Pressed --> player actions /// KEEP THAT, MIGHT HELP##
    player_action = pygame.key.get_pressed ()

    if player_action [pygame.K_LEFT] :
        plyrX = plyrX - inc
    if player_action [pygame.K_RIGHT] :
       plyrX = plyrX + inc
    if player_action [pygame.K_UP] :
        plyrY = plyrY - inc
    if player_action [pygame.K_DOWN] :
        plyrY = plyrY + inc

       
    ## Drawing and refreshing ##

    #Delete pieces then reprint

    win.fill((0,0,0))  ##REPLACE BY --> RECREATE MAZE OR WHATEVER
    pygame.draw.rect(win, (255,255,255), (plyrX , plyrY , plyrWDTH , plyrHGHT))
    pygame.draw.rect(win, (255,0,0), (pnjX , pnjY , pnjWDTH , pnjHGHT))

    pygame.display.update()