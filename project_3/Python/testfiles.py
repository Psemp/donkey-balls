import pygame
import math
import random
import pathlib
from pathlib import Path
from get_char_pos import get_char_position
from get_items import get_items_coords

class Items:

    def __init__(self):
        self.gathered = False
        self.coordinates = []        

Needle = Items()
Container = Items()
Ether = Items ()

get_items_coords(Needle,Container,Ether)

print(Needle.coordinates,Container.coordinates,Ether.coordinates)