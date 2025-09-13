import pygame as pg

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, 1, 1, _, _, _, _, _, 1, 1, _, _, _, 1], 
    [1, _, _, _, 1, _, _, _, _, _, 1, _, _, _, _, 1], 
    [1, _, 1, 1, 1, _, _, _, _, _, 1, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1], 
    [1, _, _, _, _, _, _, _, 1, _, _, _, _, 1, _, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game) -> None:               # initialization of Map in game
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for yAxis, row in enumerate(self.mini_map):     # for (variables) in (iteration, start=0), 
            for xAxis, value in enumerate(row):
                if value:
                    self.world_map[(xAxis,yAxis)] = value

    def draw(self):
                # Rectangle attrb:(screen, color, pos x-axis, pos y-axis, length, width), thickness
        [pg.draw.rect(self.game.screen, 'white', (pos[0] * 100, pos[1]* 100, 100, 100), 2)
         for pos in self.world_map]