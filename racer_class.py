# base models of all the visual components - vehicle and wall sprites
import pygame as pg
import numpy as np

class Racer(pg.sprite.Sprite):
    image = pg.Surface((20, 20), pg.SRCALPHA)
    pg.draw.polygon(image, pg.Color('white'),
                    [(20, 10), (0, 0), (4, 10), (0, 20)])

    def __init__(self, x, y, width, height, dt):
        super().__init__()
        self.pos = pg.Vector2(x, y)
        dx = (np.random.rand() - 0.5) * 2
        dy = (np.random.rand() - 0.5) * 2
        ddx = (np.random.rand() - 0.5) * 2
        ddy = (np.random.rand() - 0.5) * 2

        self.dt = dt
        self.vel = pg.Vector2(dx, dy)
        self.acc = pg.Vector2(ddx, ddy)
        
        self.rect = self.image.get_rect(center=self.pos)
        _, orient = self.vel.as_polar()
        self.image = pg.transform.rotate(Racer.image, -orient)
        self.sc_width = width
        self.sc_height = height
        self.perception_r = 150
        self.max_speed = 10
        self.max_acc = 1.5

    def move(self):
        self.pos += self.vel*self.dt + 0.5*self.acc*self.dt*self.dt
        self.vel += self.acc*self.dt
        _, orient = self.vel.as_polar()
        self.image = pg.transform.rotate(Racer.image, -orient)
        self.rect.center = self.pos
        if np.linalg.norm(self.vel) > self.max_speed:
            self.vel = self.vel / np.linalg.norm(self.vel) * self.max_speed

    def wrap(self):
        if self.pos.x < 0:
            self.pos.x += self.sc_width
        elif self.pos.x > self.sc_width:
            self.pos.x -= self.sc_width

        if self.pos.y < 0:
            self.pos.y += self.sc_height
        elif self.pos.y > self.sc_height:
            self.pos.y -= self.sc_height
