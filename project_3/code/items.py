from get_items import get_items_coords


class Items:

    def __init__(self):
        self.gathered = False
        self.coordinates = []


needle = Items()
container = Items()
ether = Items()

syringe_created = False
game_over = False

get_items_coords(needle, container, ether)
