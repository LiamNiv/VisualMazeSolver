import pygame
from sys import exit
from maze import Maze
from maze import CellType, Cell
from state import State, StateManager

# Constants
DEFAULT_DISPLAY_WIDTH = 1280
DEFAULT_DISPLAY_HEIGHT = 720
ASPECT_RATIO = 16 / 9


def init_display():
    screen = pygame.display.set_mode((DEFAULT_DISPLAY_WIDTH, DEFAULT_DISPLAY_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('VisualMazeSolver')
    return screen

def handle_window_events(screen, events):
    for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                # Keep the aspect ratio
                # screen too wide
                if width / height > ASPECT_RATIO:
                    width = int(height * ASPECT_RATIO)
                # screen too tall
                else:
                    height = int(width / ASPECT_RATIO)
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    return screen

def maze_creation_events(maze, events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Mouse left button clicked")
                pos = pygame.mouse.get_pos()
                pos = maze.which_cell_clicked(pos)
                if pos is not None:
                    row_index, col_index = pos
                    if maze[row_index, col_index].cell_type == CellType.EMPTY:
                        maze[row_index, col_index] = CellType.WALL
                    elif maze[row_index, col_index].cell_type == CellType.WALL:
                        maze[row_index, col_index] = CellType.EMPTY

       
def main():

    pygame.init()
    screen = init_display()
    clock = pygame.time.Clock()

    state_manager = StateManager()

    while True:
        # handle mandatory events
        events = pygame.event.get()
        screen = handle_window_events(screen, events)
        screen_aspect_ration_multiplier = screen.get_width() // 16

        if state_manager.get_state() == State.MAINMENU:
            pass   

        elif state_manager.get_state() == State.MAZECREATION: 
            # if needed, create a new maze
            if state_manager.is_maze_created == False:
                maze = Maze(10, 10)
                state_manager.is_maze_created = True
            # handle maze creation events
            maze_creation_events(maze, events)

            screen.fill((0, 0, 0))
            maze.update_size(screen_aspect_ration_multiplier)
            maze.draw(screen)
            
        elif state_manager.get_state() == State.MAZESOLVING:
            pass

        elif state_manager.get_state() == State.FINISHED:
            pass

        pygame.display.update()
        clock.tick(60)  # 60 tick per second

if __name__ == '__main__':
    main()
