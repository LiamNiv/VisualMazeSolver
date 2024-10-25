from enum import Enum, auto

class State(Enum):
    MAINMENU = auto()
    MAZECREATION = auto()
    MAZESOLVING = auto()
    FINISHED = auto()
    

class StateManager:
    def __init__(self):
        self.state = State.MAINMENU
        self.is_maze_created = False

    def set_state(self, state):

        if not isinstance(state, State):
            raise ValueError("State must be of type State")

        self.state = state

    def get_state(self):
        return self.state
