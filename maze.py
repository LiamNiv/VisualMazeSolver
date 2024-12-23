import pygame
from cell import Cell, CellType

class Maze(pygame.sprite.Group):

    def __init__(self, columns, rows):
        super().__init__()
        self.has_start = False
        self.has_finish = False
        self.start_pos = None
        self.finish_pos = None
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
        
        # handling "fake" replacement
        if self.grid[row][col].cell_type == value:
            return

        # handling adding START and FINISH cells
        if value == CellType.START:
            if self.has_start:
                raise ValueError("Maze already has a start cell")
            self.has_start = True
            self.start_pos = (row, col)

        if value == CellType.FINISH:
            if self.has_finish:
                raise ValueError("Maze already has a finish cell")
            self.has_finish = True
            self.finish_pos = (row, col)

        # handling removing START and FINISH cells
        if self.grid[row][col].cell_type == CellType.START:
            self.has_start = False
            self.start_pos = None
        
        if self.grid[row][col].cell_type == CellType.FINISH:
            self.has_finish = False
            self.finish_pos = None

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
        self.has_start = False
        self.has_finish = False

    def update_size(self, screen_aspect_ratio_multiplier):
        width = screen_aspect_ratio_multiplier * 8 // self.columns
        height = screen_aspect_ratio_multiplier * 8 // self.rows
        x = screen_aspect_ratio_multiplier * 4
        y = screen_aspect_ratio_multiplier // 2
        for row in self.grid:
            x_per_row = x
            for cell in row:
                cell.image = pygame.transform.scale(cell.original_image, (width, height))
                cell.rect = cell.image.get_rect()
                cell.rect.topleft = (x_per_row, y)
                x_per_row += width
            y += height

    def draw(self, screen):
        # draw the maze on the screen
        for row in self.grid:
            for cell in row:
                screen.blit(cell.image, cell.rect.topleft)

    def which_cell_clicked(self, pos):
        # return the indexes of the cell that contains the position pos
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                if cell.rect.collidepoint(pos):
                    return (row_index, col_index)
        return None

    def get_start_pos(self):
        if not self.has_start:
            raise ValueError("Maze does not have a start cell")
        return self.start_pos
    
    def get_end_pos(self):
        if not self.has_finish:
            raise ValueError("Maze does not have a finish cell")
        return self.finish_pos
