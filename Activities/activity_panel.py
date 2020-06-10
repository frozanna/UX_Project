import pygame
from Windows.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class AcitivityPanel:
    def __init__(self, name, screen, active=False):
        self.name = name
        self.screen = screen
        self.x = 7
        self.y = 75
        self.active = active
        heading_delta = 40
        section_delta = 25

        if name == "date_1":
            self.image_n = pygame.image.load('Images/date1.png')
            self.image_y = pygame.image.load('Images/date1.png')
            self.y = 30
            self.x = 25
        elif name == "you_have_1":
            self.image_n = pygame.image.load('Images/you_have_1.png')
            self.image_y = pygame.image.load('Images/you_have_1.png')
            self.y = 50 + heading_delta
            self.x = 0
        elif name == "greek_salad":
            self.image_n = pygame.image.load('Images/act_1_n.png')
            self.image_y = pygame.image.load('Images/act_1_y.png')
            self.y = 95 + heading_delta
        elif name == "skinny_alfredo":
            self.image_n = pygame.image.load('Images/act_2_n.png')
            self.image_y = pygame.image.load('Images/act_2_y.png')
            self.y = 247 + heading_delta
        elif name == "go_walk":
            self.image_n = pygame.image.load('Images/act_3_n.png')
            self.image_y = pygame.image.load('Images/act_3_y.png')
            self.y = 399 + heading_delta
        elif name == "you_have_2":
            self.image_n = pygame.image.load('Images/you_have_2.png')
            self.image_y = pygame.image.load('Images/you_have_2.png')
            self.y = 452 + heading_delta + section_delta
            self.x = 0
        elif name == "cardio":
            self.image_n = pygame.image.load('Images/act_4_n.png')
            self.image_y = pygame.image.load('Images/act_4_y.png')
            self.y = 497 + heading_delta + section_delta
        elif name == "exam":
            self.image_n = pygame.image.load('Images/act_5_n.png')
            self.image_y = pygame.image.load('Images/act_5_y.png')
            self.y = 551 + heading_delta + section_delta
        elif name == "you_have_3":
            self.image_n = pygame.image.load('Images/you_have_3.png')
            self.image_y = pygame.image.load('Images/you_have_3.png')
            self.y = 604 + heading_delta + 2 * section_delta
            self.x = 0
        elif name == "sleep":
            self.image_n = pygame.image.load('Images/act_6_n.png')
            self.image_y = pygame.image.load('Images/act_6_y.png')
            self.y = 649 + heading_delta + 2 * section_delta
        elif name == "date_2":
            self.image_n = pygame.image.load('Images/date.png')
            self.image_y = pygame.image.load('Images/date.png')
            self.y = 700 + 2 * heading_delta + 2 * section_delta
            self.x = 25
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
            pygame.draw.rect(self.screen, (255, 255, 255),
                             self.image_y_rect, 1)
        else:
            self.screen.blit(self.image_n, self.image_n_rect)
            pygame.draw.rect(self.screen, (255, 255, 255),
                             self.image_n_rect, 1)

    def pressed(self, mouse_pos):
        if self.name not in ["you_have_1", "you_have_2", "you_have_3"]:
            if self.active:
                return self.image_y_rect.collidepoint(mouse_pos)
            else:
                return self.image_n_rect.collidepoint(mouse_pos)
        else:
            return False
