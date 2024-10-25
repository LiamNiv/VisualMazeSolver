import pygame
from enum import Enum, auto

class CellType(Enum):
    EMPTY = auto()
    WALL = auto()
    START = auto()
    FINISH = auto()

    def __str__(self):
        if self == Cell.EMPTY:
            return 'E'
        elif self == Cell.WALL:
            return 'W'
        elif self == Cell.START:
            return 'S'
        elif self == Cell.FINISH:
            return 'F'
    

class Cell(pygame.sprite.Sprite):

    def __init__(self, cell_type, x_pos, y_pos, width, height):
        super().__init__()
        
        # Cell type (empty, wall, start, finish)
        self.cell_type = cell_type

        # Cell image
        if cell_type == CellType.EMPTY:
            self.image = pygame.image.load('images/empty.png').convert_alpha()
        elif cell_type == CellType.WALL:
            self.image = pygame.image.load('images/wall.png').convert_alpha()
        elif cell_type == CellType.START:
            self.image = pygame.image.load('images/start.png').convert_alpha()
        elif cell_type == CellType.FINISH:
            self.image = pygame.image.load('images/finish.png').convert_alpha()

        # Resize the image
        self.image = pygame.transform.scale(self.image, (width, height))

        # Cell position
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)

