import sys
import pygame
from settings import Settings
from ship import Ship
# pylint: disable=no-member

class AlienInvasion:
    """class for resources and game behavior"""

    def __init__(self):
        """game initialization and create game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Babilon-5. Alien invasion")
        self.screen.fill(self.settings.bg_color)
        self.ship = Ship(self)

    def run_game(self):
        """main game cycle"""
        while True:
            # check keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # visualisation last drow display
            self.ship.blitme()
            # self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == "__main__":
    # create instance and game run
    ai = AlienInvasion()
    ai.run_game()