import pathlib


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
                if character == '.' or character == 'J' or character == 'G':
                    self.floors.append(cell)
                elif character == '+':
                    self.walls.append(cell)
                if map_x == 480:
                    map_x = 0
                else:
                    map_x += map_inc
            map_y += map_inc


maze_path = pathlib.Path(__file__).parent.joinpath('maze.txt')

board = Map(open(maze_path))
