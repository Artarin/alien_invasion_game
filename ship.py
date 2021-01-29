import pygame
class Ship():
    """Class for spaceship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.ship_image = pygame.image.load('images/star_fury.png').convert()
        self.ship_image.set_colorkey((0, 0, 0))
        self.ship_image = pygame.transform.scale(self.ship_image, (100, 60))
        self.rect = self.ship_image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.start_position_x = self.rect.x
        self.start_position_y = self.rect.y
        self.x_coord = float(self.rect.x)
        self.y_coord = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.teleport = False

    def update_position(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x_coord += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x_coord -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            # "-" because coordinates come from upper left angle
            self.y_coord -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y_coord += self.settings.ship_speed
        if self.teleport:
            print (f"teleport from {self.rect.x} to {self.start_position_x}")
            self.x_coord = self.start_position_x
            self.y_coord = self.start_position_y
            self.teleport = False
        self.rect.x = self.x_coord
        self.rect.y = self.y_coord
        
    def blitme(self):
        self.screen.blit(self.ship_image, self.rect)