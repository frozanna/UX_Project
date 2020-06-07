import pygame
from Windows.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class ErrorPanel:
    def __init__(self, name, screen):
        self.name = name
        self.screen = screen
        self.x = 0
        self.y = 50

        if name == "error_panel":
            self.image = pygame.image.load('Images/404_alert.png')
        else:
            raise ValueError("Incorrect error panel type")

        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.x
        self.image_rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.image_rect)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         self.image_rect, 1)
