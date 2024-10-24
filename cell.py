from enum import Enum, auto

class Cell(Enum):
    EMPTY = auto()
    WALL = auto()
    START = auto()
    FINISH = auto()
