import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, text, x, y, width=100, height=50, button_color_passive=(0, 0, 0), button_color_active=(40, 40, 40), text_color=(255, 255, 255), text_size=25):
        super().__init__()
        # setting up the square
        self.button_rect = pygame.rect.Rect(0, 0, width, height)
        self.button_rect.center = (x, y)

        # colors for rect

        self.color_passive = button_color_passive
        self.color_active = button_color_active
        self.color = button_color_passive

        # setting up the text
        self.text  = text
        self.text_color = text_color
        button_text_font = pygame.font.Font('graphics/Pixeltype.ttf', text_size)
        self.button_text_surf = button_text_font.render(
            text, False, text_color)
        self.button_text_rect = self.button_text_surf.get_rect(
            center=self.button_rect.center)

    def update(self, x=None, y=None, screen_aspect_ratio_multiplier=None):
        """if the mouse is on top of the button, it changes the current color attribute
        """
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.color = self.color_active
        else:
            self.color = self.color_passive

        # Adjusting position if needed
        if x is not None and y is not None:
            self.button_rect.center = (x, y)
            self.button_text_rect.center = self.button_rect.center

        # Adjusting the size if needed
        if screen_aspect_ratio_multiplier is not None:
            # Adjusting the size of the button
            self.button_rect.width = screen_aspect_ratio_multiplier // 1.5
            self.button_rect.height = screen_aspect_ratio_multiplier // 3
            self.button_text_surf = pygame.transform.scale(self.button_text_surf, (screen_aspect_ratio_multiplier, screen_aspect_ratio_multiplier))
            self.button_text_rect = self.button_text_surf.get_rect(center=self.button_rect.center)

            # Adjusting the size of the text
            new_text_size = screen_aspect_ratio_multiplier // 3
            button_text_font = pygame.font.Font('graphics/Pixeltype.ttf', new_text_size)
            self.button_text_surf = button_text_font.render(self.text, False, self.text_color)
            self.button_text_rect = self.button_text_surf.get_rect(center=self.button_rect.center)
            

    def draw(self, screen):
        """drawing the button on screen using its current color
        """
        pygame.draw.rect(screen, self.color, self.button_rect)
        screen.blit(self.button_text_surf, self.button_text_rect)