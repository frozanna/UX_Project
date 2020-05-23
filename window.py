import pygame
import sys
import pygame.gfxdraw
from constant import WINDOW_HEIGHT, WINDOW_WIDTH
from menu_button import MenuButton


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.fill((255, 255, 255))
        self.basic_font = pygame.font.Font('Fonts/OpenSans-Regular.ttf', 25)
        self.menu_buttons = [MenuButton("activities", self.screen, True),
                        MenuButton("planer", self.screen, False),
                        MenuButton("food", self.screen, False),
                        MenuButton("sport", self.screen, False),
                        MenuButton("social", self.screen, False),
                        MenuButton("settings", self.screen, False)]

    def draw_frame(self):
        phone_bar_img = pygame.image.load('Images/phone_bar.png')
        self.screen.blit(phone_bar_img, (0, 0))

        menu_bar_img = pygame.image.load('Images/menu_bar.png')
        menu_h = menu_bar_img.get_height()
        self.screen.blit(menu_bar_img, (0, WINDOW_HEIGHT - menu_h))

        for button in self.menu_buttons:
            button.draw()

    def check_menu_buttons(self, mouse_pos):
        selected = None
        for button in self.menu_buttons:
            if button.pressed(mouse_pos):
                selected = button

        if selected:
            for button in self.menu_buttons:
                if selected == button:
                    button.active = True
                else:
                    button.active = False

        if selected.is_activities():
            pass #draw proper elements

    def run(self):
        self.draw_frame()
        while True:
            self.screen.fill((255, 255, 255))
            self.draw_frame()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    self.check_menu_buttons(mouse_pos)