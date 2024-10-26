import pygame
from sys import exit
from maze import Maze
from maze import CellType, Cell
from state import State, StateManager
from button import Button

# Constants
DEFAULT_DISPLAY_WIDTH = 1280
DEFAULT_DISPLAY_HEIGHT = 720
ASPECT_RATIO = 16 / 9

background_surf_original = pygame.image.load('graphics/background.png')


def init_display():
    screen = pygame.display.set_mode((DEFAULT_DISPLAY_WIDTH, DEFAULT_DISPLAY_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('VisualMazeSolver')
    return screen

def display_msg(screen, msg, time_in_ms, screen_aspect_ratio_multiplier):
    font = pygame.font.Font('graphics/Pixeltype.ttf', screen_aspect_ratio_multiplier // 2)
    text_surf = font.render(msg, True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=(screen_aspect_ratio_multiplier * 8, screen_aspect_ratio_multiplier // 4))
    screen.blit(text_surf, text_rect)
    pygame.display.update()
    pygame.time.delay(time_in_ms)

def update_base_window(screen, events):
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

    background_image = pygame.transform.scale(background_surf_original, (screen.get_width(), screen.get_height()))
    screen.blit(background_image, (0, 0))
    
    return screen

def maze_creation_events(maze, events, screen):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # left click
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                cell_index = maze.which_cell_clicked(mouse_pos)
                # if a cell is clicked
                if cell_index is not None:
                    row_index, col_index = cell_index
                    if maze[row_index, col_index].cell_type == CellType.WALL:
                        maze[row_index, col_index] = CellType.EMPTY
                    elif maze[row_index, col_index].cell_type == CellType.EMPTY:
                        maze[row_index, col_index] = CellType.WALL
                    else:
                        maze[row_index, col_index] = CellType.EMPTY
            # right click
            elif event.button == 3:
                mouse_pos = pygame.mouse.get_pos()
                cell_index = maze.which_cell_clicked(mouse_pos)
                if cell_index is not None:
                    row_index, col_index = cell_index

                    cell_center_left_pos = maze[row_index, col_index].rect.midleft
                    cell_center_right_pos = maze[row_index, col_index].rect.midright

                    # set up special choice between start and finish
                    start_button = Button('Start', cell_center_left_pos[0], cell_center_left_pos[1])
                    finish_button = Button('Finish', cell_center_right_pos[0], cell_center_right_pos[1])

                    # wait for user to choose between start and finish, or to cancel
                    while True:
                        # handle mandatory events
                        did_user_click = False
                        events = pygame.event.get()
                        screen = update_base_window(screen, events)
                        screen_aspect_ratio_multiplier = screen.get_width() // 16

                        # for updating the buttons
                        cell_center_left_pos = maze[row_index, col_index].rect.midleft
                        cell_center_right_pos = maze[row_index, col_index].rect.midright

                        for event in events:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    mouse_pos = pygame.mouse.get_pos()
                                    try:
                                        if start_button.button_rect.collidepoint(mouse_pos):
                                            maze[row_index, col_index] = CellType.START
                                        elif finish_button.button_rect.collidepoint(mouse_pos):
                                            maze[row_index, col_index] = CellType.FINISH
                                    except ValueError:
                                        display_msg(screen, "Maze already has a start or finish cell", 1500, screen_aspect_ratio_multiplier)
                                did_user_click = True   
                                break   
                        maze.update_size(screen_aspect_ratio_multiplier)
                        maze.draw(screen)
                        start_button.update(cell_center_left_pos[0], cell_center_left_pos[1], screen_aspect_ratio_multiplier)
                        finish_button.update(cell_center_right_pos[0], cell_center_right_pos[1], screen_aspect_ratio_multiplier)
                        start_button.draw(screen)
                        finish_button.draw(screen)
                        pygame.display.update()
                        if did_user_click:
                            break
                

def main():

    pygame.init()
    screen = init_display()
    clock = pygame.time.Clock()

    state_manager = StateManager()

    while True:
        # handle mandatory events
        events = pygame.event.get()
        screen = update_base_window(screen, events)
        screen_aspect_ratio_multiplier = screen.get_width() // 16

        # scale and load backgound image
        background_image = pygame.transform.scale(background_surf_original, (screen.get_width(), screen.get_height()))
        screen.blit(background_image, (0, 0))

        if state_manager.get_state() == State.MAINMENU:
            pass

        elif state_manager.get_state() == State.MAZECREATION: 
            # if needed, create a new maze
            if state_manager.is_current_state_initialized() == False:
                maze = Maze(10, 10)
                state_manager.set_current_state_initialized(True)
            # handle maze creation events
            maze_creation_events(maze, events, screen)

            maze.update_size(screen_aspect_ratio_multiplier)
            maze.draw(screen)
            
        elif state_manager.get_state() == State.MAZESOLVING:
            pass

        elif state_manager.get_state() == State.FINISHED:
            pass

        pygame.display.update()
        clock.tick(60)  # 60 tick per second

if __name__ == '__main__':
    main()
