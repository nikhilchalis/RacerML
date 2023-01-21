# base models of all the visual components - vehicle and wall sprites

class Sprite:
    def __init__(self, type, color, pos):
        self.type = type
        self.color = color
        self.pos = pos


class Racer(Sprite):
    def __init__(self, type, color, pos, vel, acc, dt):
        super.__init__(type, color, pos)
        self.vel = vel
        self.acc = acc
        self.dt = dt

    def move(self):
        self.pos += self.vec*self.dt + 0.5*self.acc*self.dt*self.dt
