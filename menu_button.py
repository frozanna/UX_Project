import pygame
from constant import WINDOW_HEIGHT, WINDOW_WIDTH


class MenuButton:
    def __init__(self, name, screen, active=False):
        self.name = name
        self.screen = screen
        start_x = 35
        space_x = 57
        self.active = active
        if active:
            self.y = WINDOW_HEIGHT - 63
        else:
            self.y = WINDOW_HEIGHT - 52

        if name == "activities":
            self.image_n = pygame.image.load('Images/activities_n.png')
            self.image_y = pygame.image.load('Images/activities_y.png')
            self.x = start_x
        elif name == "planer":
            self.image_n = pygame.image.load('Images/planer_n.png')
            self.image_y = pygame.image.load('Images/planer_y.png')
            self.x = start_x + space_x
        elif name == "food":
            self.image_n = pygame.image.load('Images/food_n.png')
            self.image_y = pygame.image.load('Images/food_y.png')
            self.x = start_x + space_x * 2
        elif name == "sport":
            self.image_n = pygame.image.load('Images/sport_n.png')
            self.image_y = pygame.image.load('Images/sport_y.png')
            self.x = start_x + space_x * 3
        elif name == "social":
            self.image_n = pygame.image.load('Images/social_n.png')
            self.image_y = pygame.image.load('Images/social_y.png')
            self.x = start_x + space_x * 4
        elif name == "settings":
            self.image_n = pygame.image.load('Images/settings_n.png')
            self.image_y = pygame.image.load('Images/settings_y.png')
            self.x = start_x + space_x * 5
        else:
            raise ValueError

    def draw(self):
        if self.active:
            self.screen.blit(self.image_y, (self.x, self.y))
        else:
            self.screen.blit(self.image_n, (self.x, self.y))

    def pressed(self, mouse_pos):
        if self.active:
            return self.image_y.collidepoint(mouse_pos)
        else:
            return self.image_n.collidepoint(mouse_pos)