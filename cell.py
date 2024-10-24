from enum import Enum, auto

class Cell(Enum):
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
