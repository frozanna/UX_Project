import pygame
from constant import WINDOW_HEIGHT, WINDOW_WIDTH


class MenuButton:
    def __init__(self, name, screen, active = False):
        self.name = name
        self.screen = screen
        start_x = 37
        space_x = 5
        self.y = WINDOW_HEIGHT - 52
        if name == "activities":
            self.image_n = pygame.image.load('Images/activities_n.png')
            self.x = start_x
            self.active = active

    def draw(self):
        if self.active:
            self.screen.blit(self.image_n, (self.x, self.y)) #change to image_y
        else:
            self.screen.blit(self.image_n, (self.x, self.y))