# base models of all the visual components - vehicle and wall sprites

class Sprite:
    def __init__(self, type, color, pos):
        self.type = type
        self.color = color
        self.pos = pos


class Racer(Sprite):
    pass
