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
        self.old_time = pygame.time.get_ticks()
        self.average_fps = []
        self.max_fps = 60
    def run_game(self):
        """main game cycle"""
        while True:
            self._check_events()
            self.ship.update_position()
            self._update_screen()
            self.fps_controller()

    def _check_events(self):
            # check keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # set move flags to True if button is down
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
    def fps_controller(self):
        """ give a pause in game cycle, then it work to fast and print average fps"""
        pygame.time.Clock().tick(self.max_fps)
        self.new_time = pygame.time.get_ticks()
        self.delta_time = self.new_time - self.old_time
        
        # if self.delta_time < 16:
        #     pygame.time.wait(16 - self.delta_time)
        self.summary_time = pygame.time.get_ticks() - self.old_time
        self.old_time = self.new_time
        self.average_fps.append(self.summary_time)
        summ = 0
        for average_fp in self.average_fps:
            summ += average_fp
        print(1000//(summ/len(self.average_fps)))
        

    def _update_screen(self):
        # refresh display and drow objects
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()



if __name__ == "__main__":
    # create instance and game run
    ai = AlienInvasion()
    ai.run_game()