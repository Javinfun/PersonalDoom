import pygame as pg
import sys
from settings import *
from map import *

# game initialization
class Game:
    def __init__(self) -> None:     # initialization of pygame library
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)        # Calls Map

    def update(self):               # Updating/display screen refresh rate
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):                 # Screen display
        self.screen.fill('black')
        self.map.draw()

    def check_events(self):         # Check inputs / default exit conditions
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    
    def run(self):                  # Main Run
        while True:
            self.check_events()
            self.update()
            self.draw()

# run game class
if __name__ == '__main__':
    game = Game()
    game.run()