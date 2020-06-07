import pygame
from Windows.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class ActivityButton:

    def __init__(self, screen):
        self.screen = screen
        self.last_view = 'activities'
        self.image = pygame.image.load('Images/act_button.png')

        self.image_rect = self.image.get_rect()
        self.image_rect.x = WINDOW_WIDTH - 70
        self.image_rect.y = WINDOW_HEIGHT - 130

    def draw(self):
        self.screen.blit(self.image, self.image_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.image_rect, 1)

    def pressed(self, mouse_pos):
        return self.image_rect.collidepoint(mouse_pos)

    def change_last_view(self, view):
        if view != 'activities' and view != 'calendar' and view != 'day':
            return
        self.last_view = view


class CreateActivityPanel:
    def __init__(self, screen):

        self.screen = screen
        self.x = 0
        self.y = 30
        self.image = pygame.image.load('Images/add_act_view.png')

        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.x
        self.image_rect.y = self.y

        self.img_add = pygame.image.load('Images/add_act_b.png')
        self.add_rect = self.img_add.get_rect()
        self.add_rect.x = 50
        self.add_rect.y = 555

        self.img_cancel = pygame.image.load('Images/cancel_act_b.png')
        self.cancel_rect = self.img_cancel.get_rect()
        self.cancel_rect.x = 200
        self.cancel_rect.y = 555

    def draw(self):
        self.screen.blit(self.image, self.image_rect)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         self.image_rect, 1)

        self.screen.blit(self.img_add, self.add_rect)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         self.add_rect, 1)

        self.screen.blit(self.img_cancel, self.cancel_rect)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         self.cancel_rect, 1)

    def buttons_pressed(self, mouse_pos):
        return self.cancel_rect.collidepoint(mouse_pos) or self.add_rect.collidepoint(mouse_pos)