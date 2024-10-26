from enum import Enum, auto

class State(Enum):
    MAINMENU = auto()
    MAZECREATION = auto()
    MAZESOLVING = auto()
    FINISHED = auto()
    

class StateManager:
    def __init__(self):
        self.current_state = State.MAZECREATION # only for now, should be MAINMENU
        self.initialized = {
            State.MAINMENU: False,
            State.MAZECREATION: False,
            State.MAZESOLVING: False,
            State.FINISHED: False
        }

    def set_current_state_initialized(self, state):
        self.initialized[self.current_state] = True

    def is_current_state_initialized(self):
        return self.initialized[self.current_state]

    def set_state(self, state):

        if not isinstance(state, State):
            raise ValueError("State must be of type State")

        self.current_state = state

    def get_state(self):
        return self.current_state
