import pygame
from Windows.constants import WINDOW_HEIGHT, WINDOW_WIDTH

class DayPanel:
    def __init__(self, name, screen, activities, active=False):
        self.name = name
        self.screen = screen
        self.x = 7
        self.y = 75
        self.active = active
        self.activities = activities

        if name == "day":
            self.image_n = pygame.image.load('Images/planner.png')
            self.image_y = pygame.image.load('Images/planner.png')
            self.y = 50
            self.x = 0
        elif name == "day_button":
            self.image_n = pygame.image.load('Images/planner_go_back.png')
            self.image_y = pygame.image.load('Images/planner_go_back.png')
            self.y = 50
            self.x = 0
        else:
            raise ValueError("Incorrect day panel type")

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
            for activity in self.activities:
                if activity == "greek_salad":
                    self.image_y = pygame.image.load('Images/plact_1.png')
                    self.drawactivity(self.image_y, 43, 235)
                elif activity == "skinny_alfredo":
                    self.image_y = pygame.image.load('Images/plact_2.png')
                    self.drawactivity(self.image_y, 43, 235)
                elif activity == "go_walk":
                    self.image_y = pygame.image.load('Images/plact_3.png')
                    self.drawactivity(self.image_y, 43, 235)
                elif activity == "cardio":
                    self.image_y = pygame.image.load('Images/plact_4.png')
                    self.drawactivity(self.image_y, 43, 390)
                elif activity == "exam":
                    self.image_y = pygame.image.load('Images/plact_5.png')
                    self.drawactivity(self.image_y, 43, 410)
                elif activity == "sleep":
                    self.image_y = pygame.image.load('Images/plact_6.png')
                    self.drawactivity(self.image_y, 43, 473)


    def pressed(self, mouse_pos):
        if self.name == "day_button":
            if self.active:
                return self.image_y_rect.collidepoint(mouse_pos)
            else:
                return self.image_n_rect.collidepoint(mouse_pos)

    def drawactivity(self, image, x, y):
        self.image_y_rect = image.get_rect()
        self.image_y_rect.x = self.x + x
        self.image_y_rect.y = self.y + y
        self.screen.blit(image, self.image_y_rect)
        pygame.draw.rect(self.screen, (245, 245, 245),
                         self.image_y_rect, 1)
