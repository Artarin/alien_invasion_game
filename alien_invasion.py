import sys
import pygame
from settings import Settings
from ship import Ship
from ship_missile import ShipMissile
from enemy import EnemyShip
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
        self.enemys = pygame.sprite.Group()
        self._create_enemy_ships()
        
    def run_game(self):
        while True:
            self._check_events()
            self.settings.fps_controller(self)
            self.ship.update_position()
            self._update_screen()
            self._check_enemy_edges()
            self._move_enemys()
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
        if event.key == pygame.K_1:
            self._move_enemys
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
            self.settings.ship_blast.play()


    def _update_missiles(self):
        self.missiles.update()
        for missile in self.missiles.copy():
            if missile.circle_center_coord[1] <= 1:
                self.missiles.remove(missile)
            for enemy in self.enemys.copy():
                missile_collide = missile.circle_center_coord.copy()
                missile_collide[0] -= enemy.rect.width / 10
                missile_collide[1] += enemy.rect.height / 2
                if enemy.rect.collidepoint(missile_collide):
                    self.settings.enemy_destroy.play()
                    self.missiles.remove(missile)
                    self.enemys.remove(enemy)
        if not self.enemys:
            self.missiles.empty()
            self._create_enemy_ships()

        
            
    def _create_enemy_ships(self):
        enemy_ship = EnemyShip(self)
        enemy_ship_wigth, enemy_ship_height  = enemy_ship.rect.size
        avialible_space_x = self.settings.screen_width - (2*enemy_ship_wigth)
        number_enemys_x = avialible_space_x // (2*enemy_ship_wigth)
        avialible_space_y = self.settings.screen_height - (
                            self.ship.rect.height + 3*enemy_ship_height)
        number_enemys_y = avialible_space_y//(2*enemy_ship_height)
        for enemy_num_y in range (number_enemys_y):
            for enemy_num_x in range (number_enemys_x):
                self._create_enemys(enemy_num_x,enemy_num_y, 
                                    enemy_ship_wigth, enemy_ship_height)
                
    def _create_enemys(self, enemy_num_x, enemy_num_y, enemy_ship_wigth,
                       enemy_ship_height ):
        enemy = EnemyShip(self)
        enemy_x = enemy_ship_wigth + 2 * enemy_ship_wigth*enemy_num_x
        enemy_y = enemy_ship_height + 2 * enemy_ship_height*enemy_num_y
        enemy.rect.x = enemy_x
        enemy.rect.y = enemy_y
        self.enemys.add(enemy)

    def _move_enemys(self):
        self.enemys.update()

    def _check_enemy_edges(self):
        for enemy in self.enemys.sprites():
            if enemy.check_edges():
                self._change_enemy_direction()
                break

    def _change_enemy_direction(self):
        for enemy in self.enemys.sprites():
            enemy.rect.y += self.settings.enemy_y_speed
        self.settings.enemy_direction *= -1

    def _update_screen(self):
        self.screen.blit(self.settings.background, (0,0))
        self.ship.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        self.screen.blit(self.settings.fps_controller(self), [0,0])
        self.enemys.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()