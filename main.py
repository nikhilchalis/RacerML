import pygame as pg
import sys
import numpy as np
from racer_class import Racer

# constants
SC_WIDTH = 1000
SC_HEIGHT = 1000
DT = 0.1


'''
# Setup
pg.init()
clock = pg.time.Clock()

# Game screen

# Initialise a racer
p_x = np.random.rand() * SC_WIDTH
p_y = np.random.rand() * SC_HEIGHT

basic_racer = Racer(p_x, p_y, SC_WIDTH, SC_HEIGHT, dt)

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
'''

def main():
    pg.init()
    sc = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
    clk = pg.time.Clock()
    sc.fill(pg.Color('black'))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    

if __name__ == "__main__":
    main()