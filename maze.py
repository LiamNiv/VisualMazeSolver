from cell import Cell

class Maze():

    def __init__(self, width, height):
        self.hasStart = False
        self.hasFinish = False
        self.width = width
        self.height = height
        self.grid = [[Cell.EMPTY for _ in range(width)] for _ in range(height)]

    def __getitem__(self, index):
        
        if not isinstance(index, tuple):
            raise ValueError("Index must be a tuple")

        row, col = index

        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            raise ValueError("Index out of grid's range")
        
        return self.grid[row][col]
    
    def __setitem__(self, index, value): 

        # handling index value errors
        if not isinstance(index, tuple):
            raise ValueError("Index must be a tuple")
        
        row, col = index

        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            raise ValueError("Index out of grid's range")

        if not isinstance(value, Cell):
            raise ValueError("Value must be of type Cell")
        
        # handling adding START and FINISH cells
        if value == Cell.START:
            if self.hasStart:
                raise ValueError("Maze already has a start cell")
            self.hasStart = True

        if value == Cell.FINISH:
            if self.hasFinish:
                raise ValueError("Maze already has a finish cell")
            self.hasFinish = True

        # handling removing START and FINISH cells
        if self.grid[row][col] == Cell.START:
            self.hasStart = False
        
        if self.grid[row][col] == Cell.FINISH:
            self.hasFinish = False

        self.grid[row][col] = value

    def __str__(self):
        # str representation of the grid
        grid_str = ''
        # horizontal border for clarity
        horizontal_border = '+---' * self.width + '+\n'

        grid_str += horizontal_border

        for row in self.grid:
            for cell in row:
                grid_str += f'| {cell} '
            grid_str += '|\n'
            grid_str += horizontal_border

        return grid_str

    def clear(self):
        # clear the grid
        self.grid = [[Cell.EMPTY for _ in range(self.width)] for _ in range(self.height)]
        self.hasStart = False
        self.hasFinish = False
