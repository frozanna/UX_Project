import pygame
import sys
import pygame.gfxdraw
from constant import WINDOW_HEIGHT, WINDOW_WIDTH
from menu_button import MenuButton
from add_activity import ActivityButton


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

                self.draw_activities()

    def draw_activities(self):
        # replace with expected data - use the wheel screen, guys!
        f = pygame.font.SysFont('', 125)
        self.wheel_screen.blit(
            f.render("Michal", True, (0, 0, 0)), (45, 100))

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
