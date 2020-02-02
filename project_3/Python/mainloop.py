import pygame
import math
import random
from pygame.locals import *

class Character:
    def __init__(self):
        self.x = 0  
        self.y = 0
        self.vel = 32
        self.alive = True

mac = Character()
guard = Character()

maze = open('maze.txt')

mapx = 0
mapy = 0
mapinc = 32

for r in maze:
    for c in r:
        if c == 'J':
            mac.x = mapx
            mac.y = mapy
        if mapx == 480:
            mapx = 0
        else:
            mapx += mapinc
    mapy += mapinc

macpos = [mac.x,mac.y]
# print(macpos)

mapx = 0
mapy = 0

maze = open('maze.txt')

for r in maze:
    for c in r:
        if c == 'G':
            guard.x = mapx
            guard.y = mapy
        if mapx == 480:
            mapx = 0
        else:
            mapx += mapinc
    mapy += mapinc

guardpos = [guard.x,guard.y]
# print(guardpos)

class Map:

    floors = []
    walls = []

    def __init__(self, maze):
        map_x = 0
        map_y = 0
        map_inc = 32
        
        for row in maze:
            for character in row:
                cell = (map_x, map_y)
                if character == '.' or character =='J' or character =='G':
                    self.floors.append(cell)
                elif character == '+':
                    self.walls.append(cell)
                if map_x == 480:
                    map_x = 0
                else:
                    map_x += map_inc
            map_y += map_inc

    def get_cell(self, x, y):
        pass

board = Map(open('maze.txt'))

FloorList = []
ItemsCoords = []

class Items:

    def __init__(self):
        self.gathered = False ##check this boolean before displaying
        self.coordinates = []        

Needle = Items()
Container = Items()
Ether = Items ()

SyringeCreated = False

maze = open('maze.txt')

mapx = 0
mapy = 0
mapinc = 32

for r in maze:
    for c in r:
        if c == '.':
            FloorList.append((mapx,mapy))
        else:
            pass
        if mapx == 480:
            mapx = 0
        else:
            mapx += mapinc 
    mapy += mapinc

ItemsCoords = random.sample(FloorList,3)
Needle.coordinates = ItemsCoords[0]
Container.coordinates = ItemsCoords[1]
Ether.coordinates = ItemsCoords [2]

class Prediction:
    def __init__(self):
        self.left = macpos
        self.right = macpos
        self.up = macpos
        self.down = macpos

pygame.init

win = pygame.display.set_mode ((480,512))

run = True
floor = pygame.image.load("images/floor.png").convert()
wall = pygame.image.load("images/wall.png").convert()
plyr = pygame.image.load("images/plyr.png").convert_alpha()
ether = pygame.image.load("images/ether.png").convert_alpha()
needle = pygame.image.load("images/needle.png").convert_alpha()
cont = pygame.image.load("images/container.png").convert_alpha()
guardimg = pygame.image.load("images/guard.png").convert_alpha()
syringe = pygame.image.load("syringe.png").convert_alpha()

while run == True:
    
    pygame.time.delay (100)

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False

    Tuple_macpos = tuple(macpos)

    if mac.alive == True and guard.alive == True and macpos == guardpos and SyringeCreated == False:
        mac.alive = False 
    if mac.alive == True and guard.alive == True and macpos == guardpos and SyringeCreated == True:
        guard.alive = False
    if  mac.alive == True and Needle.gathered == True and Ether.gathered == True and Container.gathered == True:
        SyringeCreated = True
    if mac.alive == True and Needle.gathered == False and Tuple_macpos == Needle.coordinates:
        Needle.gathered = True
    if mac.alive == True and Ether.gathered == False and Tuple_macpos == Ether.coordinates:
        Ether.gathered = True
        print("test done")
    if mac.alive == True and Container.gathered == False and Tuple_macpos == Container.coordinates:
        Container.gathered = True

    ##DRAW##

    win.fill((255,255,255))

    for i in range(0,len(board.floors)):
        win.blit(floor,(board.floors[i]))

    for i in range(0,len(board.walls)):
        win.blit(wall,(board.walls[i]))

    if Ether.gathered == False:
        win.blit(ether, (Ether.coordinates))
    else:
        win.blit(ether, (0,480))

    if Needle.gathered == False:
        win.blit(needle, (Needle.coordinates))  
    else:
        win.blit(needle, (32,480))

    if Container.gathered == False:
        win.blit(cont, (Container.coordinates))
    else:
        win.blit(cont, (64,480))
    
    if SyringeCreated == True:
        win.blit(syringe, (416,480))

    if mac.alive == True:
        win.blit(plyr, (macpos))

    if guard.alive == True:
        win.blit(guardimg, (guardpos))

    ##/DRAW##

    player_action = pygame.key.get_pressed()

    Predict = Prediction()
    Predict.left[0] = Predict.left[0] - mac.vel
    Predict.right[0] = Predict.right[0] + mac.vel
    Predict.up[1] = Predict.up[1] - mac.vel
    Predict.down[1] = Predict.left[1] + mac.vel

    print(Predict.left)


    if player_action [pygame.K_LEFT] :
        macpos[0] = macpos[0] - mac.vel
    if player_action [pygame.K_RIGHT] :
        macpos[0] = macpos[0] + mac.vel
    if player_action [pygame.K_UP] :
        macpos[1] = macpos[1] - mac.vel
    if player_action [pygame.K_DOWN] :
        macpos[1] = macpos[1] + mac.vel

    pygame.display.flip()