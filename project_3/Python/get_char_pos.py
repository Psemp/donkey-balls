import pathlib
from pathlib import Path

Maze_Path = pathlib.Path(__file__).parent.joinpath('maze.txt')

maze = open(Maze_Path)

mapx = 0
mapy = 0
mapinc = 32

char.x = 0
char.y = 0

def get_char_position(char):
    for r in maze:
        for c in r:
            if c == 'J' and char == "mac":
                char.x = mapx
                char.y = mapy
            elif c == 'G' and char == "guard":
                char.x = mapx
                char.y = mapy
            if mapx == 480:
                mapx = 0
            else:
                mapx += mapinc
        mapy += mapinc

charpos = [char.x,char.y]
return charpos