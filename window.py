import pygame
import sys
import pygame.gfxdraw
from constant import WINDOW_HEIGHT, WINDOW_WIDTH
from menu_button import MenuButton
from add_activity import ActivityButton


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
        self.activity_button = ActivityButton(self.screen)

    def draw_frame(self):  # draw all elements that should be always visible
        phone_bar_img = pygame.image.load('Images/phone_bar.png')
        self.screen.blit(phone_bar_img, (0, 0))

        menu_bar_img = pygame.image.load('Images/menu_bar.png')
        menu_h = menu_bar_img.get_height()
        self.screen.blit(menu_bar_img, (0, WINDOW_HEIGHT - menu_h))

        self.activity_button.draw()

        for button in self.menu_buttons:
            button.draw()

    def check_menu_buttons(self, mouse_pos):  # checks if user clicked on some item in menu
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
                pass  # draw proper elements

    def check_activity_button(self, mouse_pos):
        if self.activity_button.pressed(mouse_pos):
            pass # do something maybe

    def run(self):
        self.draw_frame()
        while True:
            self.screen.fill((255, 255, 255))  # reset screen after each frame
            # here should we draw other items, such as activities cards, calendar etc.
            self.draw_frame()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    self.check_menu_buttons(mouse_pos)
                    self.check_activity_button(mouse_pos)