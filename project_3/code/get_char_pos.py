import pathlib


def get_char_position(char):

    Maze_Path = pathlib.Path(__file__).parent.joinpath('maze.txt')

    maze = open(Maze_Path)

    mapx = 0
    mapy = 0
    mapinc = 32

    for r in maze:
        for c in r:
            if c == 'J' and char.tag == "mac":
                char.x = mapx
                char.y = mapy
            elif c == 'G' and char.tag == "guard":
                char.x = mapx
                char.y = mapy
            if mapx == 480:
                mapx = 0
            else:
                mapx += mapinc
        mapy += mapinc
    charpos = [char.x, char.y]
    return charpos
