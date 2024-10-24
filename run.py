import pygame
from sys import exit
from maze import Maze

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


def main():

    pygame.init()
    screen = init_display()
    clock = pygame.time.Clock()

    while True:
        screen = handle_window_events(screen)

        pygame.display.update()
        clock.tick(60)  # 60 tick per second

if __name__ == '__main__':
    main()
