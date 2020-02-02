import random
import math

FloorList = []
ItemsCoords = []

class Items:

    def __init__(self):
        self.gathered = False ##check this boolean before displaying
        self.coordinates = []        

Needle = Items()
Container = Items()
Ether = Items ()

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
# print (ItemsCoords)
Needle.coordinates = ItemsCoords[0]
Container.coordinates = ItemsCoords[1]
Ether.coordinates = ItemsCoords [2]
# print(Needle.coordinates,Container.coordinates,Ether.coordinates)


## loop --> get floors ONLY w/o J and G
## Random 0 --> Len list-positions already picked
## 4 instances
## Syringe = 3 items set to Gathered