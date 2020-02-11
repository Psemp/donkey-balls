import random
import pathlib
from pathlib import Path


def get_items_coords(Needle,Container,Ether):

    Maze_Path = pathlib.Path(__file__).parent.joinpath('maze.txt')
    maze = open(Maze_Path)

    FloorList = []
    ItemsCoords = []
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