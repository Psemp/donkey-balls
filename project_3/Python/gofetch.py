mapx = 0
mapy = 0
mapinc = 32
maze = open('maze.txt')

class player:
    def __init__(self):
        self.x = 0  
        self.y = 0
        self.vel = 32

mac = player()

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
print(macpos)


