import pygame
from cell import Cell, CellType

class Maze(pygame.sprite.Group):

    def __init__(self, columns, rows):
        super().__init__()
        self.hasStart = False
        self.hasFinish = False
        self.columns = columns
        self.rows = rows
        self.grid = [[Cell(CellType.EMPTY) for _ in range(columns)] for _ in range(rows)]

    def __getitem__(self, index):
        
        if not isinstance(index, tuple):
            raise ValueError("Index must be a tuple")

        row, col = index

        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            raise ValueError("Index out of grid's range")
        
        return self.grid[row][col]
    
    def __setitem__(self, index, value): 

        # handling index value errors
        if not isinstance(index, tuple):
            raise ValueError("Index must be a tuple")
        
        row, col = index

        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            raise ValueError("Index out of grid's range")

        if not isinstance(value, CellType):
            raise ValueError("Value must be of type CellType")
        
        # handling "fake" replacment
        if self.grid[row][col].cell_type == value:
            return

        # handling adding START and FINISH cells
        if value == CellType.START:
            if self.hasStart:
                raise ValueError("Maze already has a start cell")
            self.hasStart = True

        if value == CellType.FINISH:
            if self.hasFinish:
                raise ValueError("Maze already has a finish cell")
            self.hasFinish = True

        # handling removing START and FINISH cells
        if self.grid[row][col] == CellType.START:
            self.hasStart = False
        
        if self.grid[row][col] == CellType.FINISH:
            self.hasFinish = False

        self.grid[row][col] = Cell(value)

    def __str__(self):
        # str representation of the grid
        grid_str = ''
        # horizontal border for clarity
        horizontal_border = '+---' * self.width + '+\n'

        grid_str += horizontal_border

        for row in self.grid:
            for cell in row:
                grid_str += f'| {cell.cell_type} '
            grid_str += '|\n'
            grid_str += horizontal_border

        return grid_str

    def clear(self):
        # clear the grid
        self.grid = [[CellType.EMPTY for _ in range(self.columns)] for _ in range(self.rows)]
        self.hasStart = False
        self.hasFinish = False

    def update_size(self, screen_aspect_ratio_multiplier):
        width = screen_aspect_ratio_multiplier * 8 // self.columns
        height = screen_aspect_ratio_multiplier * 8 // self.rows
        x = screen_aspect_ratio_multiplier * 4
        y = screen_aspect_ratio_multiplier // 2
        for row in self.grid:
            x_per_row = x
            for cell in row:
                cell.image = pygame.transform.scale(cell.image, (width, height))
                cell.rect = cell.image.get_rect()
                cell.rect.topleft = (x_per_row, y)
                x_per_row += width
            y += height

    def draw(self, screen):
        # draw the maze on the screen
        for row in self.grid:
            for cell in row:
                screen.blit(cell.image, cell.rect.topleft)
