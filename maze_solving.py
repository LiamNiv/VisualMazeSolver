from maze import Maze
from cell import Cell, CellType

def solve_maze(maze):
    # get start and end positions
    start_pos = maze.get_start_pos()
    end_pos = maze.get_end_pos()

    # note: add feature to prevent this from being called without a start and end cell

    maze_rows, maze_columns = maze.rows, maze.columns
    has_visited = [[False for _ in range(maze_columns)] for _ in range(maze_rows)]
    path = []

    def recursive_solve(pos):
        row, col = pos

        
        # failure cases
        if row < 0 or row >= maze_rows or col < 0 or col >= maze_columns:
            return False
        if has_visited[row][col]:
            return False
        if maze[row, col].cell_type == CellType.WALL:
            return False
        
        # keeping track
        has_visited[row][col] = True
        path.append((row, col))

        if pos == end_pos:
            return True
        
        neighboring_cells_pos = [
            (row - 1, col),  # up pos
            (row + 1, col),  # down pos
            (row, col - 1),  # left pos
            (row, col + 1)   # right pos
        ]

        for next_cell_pos in neighboring_cells_pos:
            if recursive_solve(next_cell_pos):
                return True
        
        # remove last item, default index val is -1
        path.pop()
        return False
    
    if recursive_solve(start_pos):
        # solution found
        return path
    else:
        # no solution found
        return None