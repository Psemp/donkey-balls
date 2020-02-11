from get_items import get_items_coords


class Items:

    def __init__(self):
        self.gath = False
        self.pos = []


needle = Items()
container = Items()
ether = Items()

get_items_coords(needle, container, ether)
