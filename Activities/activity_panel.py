import pygame
from Windows.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class AcitivityPanel:
    def __init__(self, name, screen, active=False):
        self.name = name
        self.screen = screen
        self.x = 7
        self.y = 75
        self.active = active

        if name == "greek_salad":
            self.image_n = pygame.image.load('Images/act_1_n.png')
            self.image_y = pygame.image.load('Images/act_1_y.png')
        elif name == "skinny_alfredo":
            self.image_n = pygame.image.load('Images/act_2_n.png')
            self.image_y = pygame.image.load('Images/act_2_y.png')
            self.y = 222
        elif name == "go_walk":
            self.image_n = pygame.image.load('Images/act_3_n.png')
            self.image_y = pygame.image.load('Images/act_3_y.png')
            self.y = 370
        else:
            raise ValueError("Incorrect acitivity panel type")

        self.image_n_rect = self.image_n.get_rect()
        self.image_n_rect.x = self.x
        self.image_n_rect.y = self.y
        self.image_y_rect = self.image_y.get_rect()
        self.image_y_rect.x = self.x
        self.image_y_rect.y = self.y

    def draw(self):
        if self.active:
            self.screen.blit(self.image_y, self.image_y_rect)
            pygame.draw.rect(self.screen, (245, 245, 245),
                             self.image_y_rect, 1)
        else:
            self.screen.blit(self.image_n, self.image_n_rect)
            pygame.draw.rect(self.screen, (245, 245, 245),
                             self.image_n_rect, 1)

    def pressed(self, mouse_pos):
        if self.active:
            return self.image_y_rect.collidepoint(mouse_pos)
        else:
            return self.image_n_rect.collidepoint(mouse_pos)
