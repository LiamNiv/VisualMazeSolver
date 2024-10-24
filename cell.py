import pygame
from enum import Enum, auto

class Cell(Enum, pygame.sprite.Sprite):
    EMPTY = auto()
    WALL = auto()
    START = auto()
    FINISH = auto()

    def __init__(self, x_pos, y_pos):
        super().__init__()
        
        if (self == Cell.EMPTY):
            self.image = pygame.image.load('images/empty.png').convert_alpha()
        elif (self == Cell.WALL):
            self.image = pygame.image.load('images/wall.png').convert_alpha()
        elif (self == Cell.START):
            self.image = pygame.image.load('images/start.png').convert_alpha()
        elif (self == Cell.FINISH):
            self.image = pygame.image.load('images/finish.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)

    def __str__(self):
        if self == Cell.EMPTY:
            return 'E'
        elif self == Cell.WALL:
            return 'W'
        elif self == Cell.START:
            return 'S'
        elif self == Cell.FINISH:
            return 'F'
