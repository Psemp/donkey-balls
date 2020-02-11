import random
import pathlib


def get_items_coords(needle, container, ether):

    Maze_Path = pathlib.Path(__file__).parent.joinpath('maze.txt')
    maze = open(Maze_Path)

    floor_list = []
    items_coords = []
    mapx = 0
    mapy = 0
    mapinc = 32

    for r in maze:
        for c in r:
            if c == '.':
                floor_list.append((mapx, mapy))
            else:
                pass
            if mapx == 480:
                mapx = 0
            else:
                mapx += mapinc
        mapy += mapinc

    items_coords = random.sample(floor_list, 3)
    needle.pos = items_coords[0]
    container.pos = items_coords[1]
    ether.pos = items_coords[2]
