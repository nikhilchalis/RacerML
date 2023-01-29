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
dt = 0.1

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
        
        pressed = pg.key.get_pressed()
        if (pressed[pg.K_UP] or pressed[pg.K_w]): 
            basic_racer.speed_up()
        elif (pressed[pg.K_DOWN] or pressed[pg.K_s]): 
            basic_racer.slow_down()
        elif (pressed[pg.K_LEFT] or pressed[pg.K_a]): 
            basic_racer.turn_left()
        elif (pressed[pg.K_RIGHT] or pressed[pg.K_d]): 
            basic_racer.turn_right()
        elif (pressed[pg.K_SPACE]): 
            basic_racer.warp = True
        
    pg.display.flip()
    sc.fill((0, 0, 0)) 

    basic_racer.move()
    basic_racer.wrap()
    sc.blit(basic_racer.image, basic_racer.pos)

    clock.tick(30)

# Quit Pygame
pg.quit()
