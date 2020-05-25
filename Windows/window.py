import pygame
import sys
import pygame.gfxdraw
from Windows.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from Windows.menu_button import MenuButton
from Activities.add_activity import ActivityButton
from Activities.activity_panel import AcitivityPanel


class Window:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Kwolokwium')

        # scroll screen
        self.wheel_screen = pygame.surface.Surface(
            (WINDOW_WIDTH, WINDOW_HEIGHT * 2))
        self.wheel_screen.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.scroll_y = 0

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.fill((255, 255, 255))
        self.basic_font = pygame.font.Font('Fonts/OpenSans-Regular.ttf', 25)
        self.menu_buttons = [
            MenuButton("activities", self.screen, True),
            MenuButton("planer", self.screen, False),
            MenuButton("food", self.screen, False),
            MenuButton("sport", self.screen, False),
            MenuButton("social", self.screen, False),
            MenuButton("settings", self.screen, False)
        ]

        self.activity_button = ActivityButton(self.screen)

        self.acitvities = [
            AcitivityPanel("you_have_1", self.wheel_screen, False),
            AcitivityPanel("greek_salad", self.wheel_screen, False),
            AcitivityPanel("skinny_alfredo", self.wheel_screen, False),
            AcitivityPanel("go_walk", self.wheel_screen, False),
            AcitivityPanel("you_have_2", self.wheel_screen, False),
            AcitivityPanel("cardio", self.wheel_screen, False),
            AcitivityPanel("exam", self.wheel_screen, False),
            AcitivityPanel("you_have_3", self.wheel_screen, False),
            AcitivityPanel("sleep", self.wheel_screen, False)
        ]

    # draw all elements that should be always visible
    def draw_frame(self):
        phone_bar_img = pygame.image.load('Images/phone_bar.png')
        self.screen.blit(phone_bar_img, (0, 0))

        menu_bar_img = pygame.image.load('Images/menu_bar.png')
        menu_h = menu_bar_img.get_height()
        self.screen.blit(menu_bar_img, (0, WINDOW_HEIGHT - menu_h))

        if self.menu_buttons[0].active:
            self.activity_button.draw()

        for button in self.menu_buttons:
            button.draw()

    # checks if user clicked on some item in menu
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
                self.draw_activities(mouse_pos)
            else:
                # reset screen
                self.wheel_screen.fill((255, 255, 255))

    def draw_activities(self):
        selected = None
        for activitie in self.acitvities:
            activitie.draw()


    def run(self):

        # start from activities diagram
        self.draw_activities()
        self.screen.blit(self.wheel_screen, (0, self.scroll_y))
        self.draw_frame()

        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    self.check_menu_buttons(mouse_pos)
                    # scroll control
                    if event.button == 4:
                        self.scroll_y = min(self.scroll_y + 15, 0)
                    if event.button == 5:
                        self.scroll_y = max(self.scroll_y - 15, -300)
                    self.screen.blit(self.wheel_screen, (0, self.scroll_y))
                    self.draw_frame()
                    pygame.display.flip()
                    self.clock.tick(60)