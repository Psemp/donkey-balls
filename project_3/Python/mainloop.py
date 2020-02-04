import pygame
import math
import random
import pathlib
from pathlib import Path

class Character:
    def __init__(self):
        self.x = 0  
        self.y = 0
        self.vel = 32
        self.alive = True

mac = Character()
guard = Character()

Maze_Path = pathlib.Path(__file__).parent.joinpath('maze.txt')

maze = open(Maze_Path)

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

mapx = 0
mapy = 0

maze = open(Maze_Path)

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

board = Map(open(Maze_Path))

FloorList = []
ItemsCoords = []

class Items:

    def __init__(self):
        self.gathered = False
        self.coordinates = []        

Needle = Items()
Container = Items()
Ether = Items ()

SyringeCreated = False
GameOver = False

maze = open(Maze_Path)

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

pygame.init

win = pygame.display.set_mode ((480,512))

run = True

def get_path(file_name):
    return str(Path(__file__).parent.parent.joinpath("images", file_name))

def get_image(file_name):
    return pygame.image.load(get_path(file_name)).convert()

def get_image_alpha(file_name):
    return pygame.image.load(get_path(file_name)).convert_alpha()


known_images = ['floor.png', 'wall.png']
known_alpha_images = ['plyr.png','ether.png','needle.png','container.png','guard.png','syringe.png','victory.png','defeat.png']

images = {}

for known_image in known_images:
    loaded_image = get_image(known_image)
    images[known_image] = loaded_image

for known_image in known_alpha_images:
    loaded_image = get_image_alpha(known_image)
    images[known_image] = loaded_image


while run == True:
    
    pygame.time.delay (100)

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False

    Tuple_macpos = tuple(macpos)

    if mac.alive and guard.alive and macpos == guardpos and not SyringeCreated:
        mac.alive = False
        GameOver = True 
    if mac.alive and guard.alive and macpos == guardpos and SyringeCreated:
        guard.alive = False
        GameOver = True
    if  mac.alive and Needle.gathered and Ether.gathered and Container.gathered:
        SyringeCreated = True
    if mac.alive and not Needle.gathered and Tuple_macpos == Needle.coordinates:
        Needle.gathered = True
    if mac.alive and not Ether.gathered and Tuple_macpos == Ether.coordinates:
        Ether.gathered = True
    if mac.alive and not Container.gathered and Tuple_macpos == Container.coordinates:
        Container.gathered = True

    ##DRAW##

    win.fill((255,255,255))

    for i in range(0,len(board.floors)):
        win.blit(images["floor.png"],(board.floors[i]))

    for i in range(0,len(board.walls)):
        win.blit(images["wall.png"],(board.walls[i]))

    if not Ether.gathered:
        win.blit(images["ether.png"], (Ether.coordinates))
    else:
        win.blit(images["ether.png"], (0,480))

    if not Needle.gathered:
        win.blit(images["needle.png"], (Needle.coordinates))  
    else:
        win.blit(images["needle.png"], (32,480))

    if not Container.gathered:
        win.blit(images["container.png"], (Container.coordinates))
    else:
        win.blit(images["container.png"], (64,480))
    
    if SyringeCreated:
        win.blit(images["syringe.png"], (416,480))

    if mac.alive:
        win.blit(images["plyr.png"], (macpos))

    if guard.alive:
        win.blit(images["guard.png"], (guardpos))
    
    if GameOver and mac.alive:
        win.blit(images["victory.png"], (0,0))
        
    if GameOver and not mac.alive:
        win.blit(images["defeat.png"], (0,0))

    ##/DRAW##
    
    ##MOVEMENT##

    player_action = pygame.key.get_pressed()
    
    if player_action [pygame.K_LEFT] and not GameOver:
        macpos[0] = macpos[0] - mac.vel
        if tuple(macpos) in board.walls:
            macpos[0] = macpos[0] + mac.vel

    if player_action [pygame.K_RIGHT] and not GameOver:
        macpos[0] = macpos[0] + mac.vel
        if tuple(macpos) in board.walls:
            macpos[0] = macpos[0] - mac.vel

    if player_action [pygame.K_UP] and not GameOver:
        macpos[1] = macpos[1] - mac.vel
        if tuple(macpos) in board.walls:
            macpos[1] = macpos[1] + mac.vel

    if player_action [pygame.K_DOWN] and not GameOver:
        macpos[1] = macpos[1] + mac.vel
        if tuple(macpos) in board.walls:
            macpos[1] = macpos[1] - mac.vel

    ##/MOVEMENT##

    pygame.display.flip()