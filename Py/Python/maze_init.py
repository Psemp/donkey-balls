maze = open('maze.txt')

mapx = 0
mapy = 0
mapinc = 32

class map:
    def __init__(self):
        self.listofcoords = []

floor = map()

for r in maze:
    for c in r:
        if c == '.' or c =='J' or c =='G':
            floor.listofcoords.append((mapx,mapy))
        elif c == '+':
            pass
        if mapx == 480:
            mapx = 0
        else:
            mapx += mapinc 
    mapy += mapinc

print (floor.listofcoords)