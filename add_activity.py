import pygame
from constant import WINDOW_HEIGHT, WINDOW_WIDTH


class ActivityButton:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('Images/act_button.png')

        self.image_rect = self.image.get_rect()
        self.image_rect.x = WINDOW_WIDTH - 70
        self.image_rect.y = WINDOW_HEIGHT - 130

    def draw(self):
        self.screen.blit(self.image, self.image_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.image_rect, 1)

    def pressed(self, mouse_pos):
        return self.image_rect.collidepoint(mouse_pos)