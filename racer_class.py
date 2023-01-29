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
        self.dt = dt
        self.vel = pg.Vector2(0, 0)
        self.speed = 0
        self.angle = 0
        
        self.rect = self.image.get_rect(center=self.pos)
        self.image = pg.transform.rotate(Racer.image, -self.vel[1])
        self.sc_width = width
        self.sc_height = height
        self.perception_r = 150
        self.max_speed = 10
        self.max_acc = 1.5
        self.warp = False
        self.warp_factor = 50
        self.warp_timer = 0

    def turn_right(self):
        self.angle += 10

    def turn_left(self):
        self.angle -= 10

    def speed_up(self):
        self.speed += 10

    def slow_down(self):
        self.speed -= 10

    def move(self):
        self.vel.from_polar((self.speed, self.angle))
        self.image = pg.transform.rotate(Racer.image, -self.angle)
        if self.warp and self.warp_timer <= 0:
            warp_vec = pg.Vector2(0, 0)
            warp_vec.from_polar((1, self.angle))
            self.pos += self.warp_factor * warp_vec
            self.warp_timer = 10
            self.warp = False
        elif self.warp_timer > 0:
            self.warp_timer -= self.dt

        self.pos += self.vel * self.dt
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
