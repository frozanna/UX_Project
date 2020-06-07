import pygame
from Windows.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class FriendsPanel:
    def __init__(self, name, screen):
        self.name = name
        self.screen = screen
        self.x = 0
        self.y = 50

        if name == "static_panel":
            self.image = pygame.image.load('Images/friends_static.png')
        else:
            raise ValueError("Incorrect friend panel type")

        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.x
        self.image_rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.image_rect)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         self.image_rect, 1)
