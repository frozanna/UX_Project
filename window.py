import pygame
import sys

class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((750, 1334))
        self.basic_font = pygame.font.Font('Pixeled.ttf', 25)

    def run(self):
        pygame.init()
        pygame.display.set_mode((750, 1334))
        self.font = pygame.font.Font('Pixeled.ttf', 25)