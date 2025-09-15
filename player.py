import pygame as pg
import math
from settings import *

class Player:
    def __init__(self, game) -> None:       # Initialization of player
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
    
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED + self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
    
    def update(self):
        self.movement
    
    @property
    def pos(self):                          # Returns player coordinates
        return self.x, self.y
    
    @property
    def map_pos(self):                      # Relative to map
        return int(self.x), int(self.y)