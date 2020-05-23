import pygame
from constant import WINDOW_HEIGHT, WINDOW_WIDTH


class MenuButton:
    def __init__(self, name, screen, active=False):
        self.name = name
        self.screen = screen
        start_x = 30
        space_x = 57
        self.active = active
        self.ac_y = WINDOW_HEIGHT - 63
        self.nac_y = WINDOW_HEIGHT - 52

        if name == "activities":
            self.image_n = pygame.image.load('Images/activities_n.png')
            self.image_y = pygame.image.load('Images/activities_y.png')
            self.ac_x = start_x - 5
            self.nac_x = self.ac_x + 10
        elif name == "planer":
            self.image_n = pygame.image.load('Images/planer_n.png')
            self.image_y = pygame.image.load('Images/planer_y.png')
            self.nac_x = start_x + space_x
            self.ac_x = self.nac_x - 10
        elif name == "food":
            self.image_n = pygame.image.load('Images/food_n.png')
            self.image_y = pygame.image.load('Images/food_y.png')
            self.nac_x = start_x + space_x * 2
            self.ac_x = self.nac_x - 10
        elif name == "sport":
            self.image_n = pygame.image.load('Images/sport_n.png')
            self.image_y = pygame.image.load('Images/sport_y.png')
            self.nac_x = start_x + space_x * 3
            self.ac_x = self.nac_x - 10
        elif name == "social":
            self.image_n = pygame.image.load('Images/social_n.png')
            self.image_y = pygame.image.load('Images/social_y.png')
            self.nac_x = start_x + space_x * 4
            self.ac_x = self.nac_x - 10
        elif name == "settings":
            self.image_n = pygame.image.load('Images/settings_n.png')
            self.image_y = pygame.image.load('Images/settings_y.png')
            self.nac_x = start_x + space_x * 5
            self.ac_x = self.nac_x - 10
        else:
            raise ValueError

        self.image_n_rect = self.image_n.get_rect()
        self.image_n_rect.x = self.nac_x
        self.image_n_rect.y = self.nac_y
        self.image_y_rect = self.image_y.get_rect()
        self.image_y_rect.x = self.ac_x
        self.image_y_rect.y = self.ac_y

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

    def is_activities(self):
        return self.name == "activities"
