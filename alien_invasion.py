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
        self.settings = Settings(self)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Babilon-5. Alien invasion")
        self.ship = Ship(self)
        # self.old_time = pygame.time.get_ticks()

    def run_game(self):
        """main game cycle"""
        while True:
            self._check_events()
            self.ship.update_position()
            self._update_screen()
            self.settings.fps_controller(self)
            self.settings.ship_speed_controller()
            

    def _check_events(self):
            # check keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                1# set move flags to True if button is down
                if event.key == pygame.K_q:
                    # fast close game
                    sys.exit()
                if event.key == pygame.K_t:
                    # teleport ship to start position
                    self.ship.teleport = True
                if event.key == pygame.K_RIGHT:
                    # move ship right
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    # move ship left
                    self.ship.moving_left = True
                if event.key == pygame.K_UP:
                    # move ship up
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    # move ship down
                    self.ship.moving_down = True    
            elif event.type == pygame.KEYUP:
                # set move flags to False if button is up
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _update_screen(self):
        # refresh display and drow objects
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.screen.blit(self.settings.fps_controller(self), [0,0])
        pygame.display.flip()



if __name__ == "__main__":
    # create instance and game run
    ai = AlienInvasion()
    ai.run_game()