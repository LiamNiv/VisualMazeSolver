import pygame
from enum import Enum, auto

class CellType(Enum):
    EMPTY = auto()
    WALL = auto()
    START = auto()
    FINISH = auto()

    def __str__(self):
        if self is CellType.EMPTY:
            return 'E'
        elif self is CellType.WALL:
            return 'W'
        elif self is CellType.START:
            return 'S'
        elif self is CellType.FINISH:
            return 'F'
    

class Cell(pygame.sprite.Sprite):

    def __init__(self, cell_type, x_pos = 0, y_pos = 0, width = 200, height = 200):
        super().__init__()
        
        # Cell type (empty, wall, start, finish)
        self.cell_type = cell_type

        # Cell image
        if cell_type is CellType.EMPTY:
            self.original_image = pygame.image.load('graphics/empty.png').convert_alpha()
        elif cell_type is CellType.WALL:
            self.original_image = pygame.image.load('graphics/wall.png').convert_alpha()
        elif cell_type is CellType.START:
            self.original_image = pygame.image.load('graphics/start.png').convert_alpha()
        elif cell_type is CellType.FINISH:
            self.original_image = pygame.image.load('graphics/finish.png').convert_alpha()

        # Resize the image
        self.image = pygame.transform.scale(self.original_image, (width, height))

        # Cell position
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)

    def __str__(self):
        return f"({self.cell_type}, x: {self.rect.x}, y: {self.rect.y}, width: {self.rect.width}, height: {self.rect.height})"
