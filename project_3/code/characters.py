from get_char_pos import get_char_position


class Character:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.vel = 32
        self.alive = True
        self.tag = "str"


mac = Character()


mac.tag = "mac"
guard = Character()
guard.tag = "guard"

macpos = get_char_position(mac)
guardpos = get_char_position(guard)
