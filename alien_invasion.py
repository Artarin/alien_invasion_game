import sys
import pygame
from settings import Settings
from ship import Ship
from ship_missile import ShipMissile
# pylint: disable=no-member

class AlienInvasion:
    """class for resources and game behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings(self)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Babilon-5. Starfury is under attack")
        self.ship = Ship(self)
        self.missile = ShipMissile(self)
        self.missiles = pygame.sprite.Group()
        
    def run_game(self):
        while True:
            self._check_events()
            self.settings.fps_controller(self)
            self.ship.update_position()
            self._update_screen()
            self._update_missiles()
            self.ship.apply_dtime_to_ship_speed()
            
                
            # need later add dtime for missile and for alien ships
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                 
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            self._fire_missile()
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_t:
            self.ship.teleport = True
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True 

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_missile(self):
        if len(self.missiles) < self.missile.max_on_display:
            new_missile = ShipMissile(self)
            self.missiles.add(new_missile)


    def _update_missiles(self):
        self.missiles.update()
        for missile in self.missiles.copy():
            if missile.circle_center_coord[1] <= 1:
                self.missiles.remove(missile)
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        self.screen.blit(self.settings.fps_controller(self), [0,0])
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()