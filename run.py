import pygame
from sys import exit
from maze import Maze
from maze import CellType, Cell

# Constants
DEFAULT_DISPLAY_WIDTH = 1280
DEFAULT_DISPLAY_HEIGHT = 720
ASPECT_RATIO = 16 / 9


def init_display():
    screen = pygame.display.set_mode((DEFAULT_DISPLAY_WIDTH, DEFAULT_DISPLAY_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('VisualMazeSolver')
    return screen

def handle_window_events(screen):
    for event in pygame.event.get():
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


def main():

    pygame.init()
    screen = init_display()
    clock = pygame.time.Clock()

    program_phase = "maze_creation"
    has_maze_been_created = False

    while True:
        screen = handle_window_events(screen)
        screen_aspect_ration_multiplier = screen.get_width() // 16

        if program_phase == "maze_creation":
            
            # if needed, create a new maze
            if not has_maze_been_created:
                maze = Maze(10, 10)
                has_maze_been_created = True

            screen.fill((0, 0, 0))
            maze.update_size(screen_aspect_ration_multiplier)
            maze.draw(screen)
            

        pygame.display.update()
        clock.tick(60)  # 60 tick per second

if __name__ == '__main__':
    main()
