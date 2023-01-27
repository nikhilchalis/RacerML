import pygame as pg
import sys
import numpy as np
from racer_class import Racer

# Setup
pg.init()
clock = pg.time.Clock()

# Game screen
sc_width = 1000
sc_height = 1000
sc = pg.display.set_mode((sc_width, sc_height))
dt = 0.2 

# Initialise a racer
p_x = np.random.rand() * sc_width
p_y = np.random.rand() * sc_height

basic_racer = Racer(p_x, p_y, sc_width, sc_height, dt)

# Run the game loop
running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()
    sc.fill((0, 0, 0)) 

    basic_racer.move()
    basic_racer.wrap()
    sc.blit(basic_racer.image, basic_racer.pos)

    clock.tick(10)

# Quit Pygame
pg.quit()