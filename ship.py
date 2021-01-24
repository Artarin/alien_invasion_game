import pygame
class Ship():
    """Class for driving spaceship"""
    def __init__(self, ai_game):
        """initialization  starship and set it start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship image and get rectangle.
        self.image = pygame.image.load('images/star_fury.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()
        
        # every new ship creates on bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.start_position_x = self.rect.x
        self.start_position_y = self.rect.y
        self.x_coord = float(self.rect.x)
        self.y_coord = float(self.rect.y)

        # moving flags:
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.teleport = False

    def update_position(self):
        # update x_coord and y_coord while Flag is True
        if self.moving_right:
            self.x_coord += self.settings.ship_speed
        if self.moving_left:
            self.x_coord -= self.settings.ship_speed
        if self.moving_up:
            # "-" because coordinates come from upper left angle
            self.y_coord -= self.settings.ship_speed
        if self.moving_down:
            self.y_coord += self.settings.ship_speed
        if self.teleport:
            print (f"teleport from {self.rect.x} to {self.start_position_x}")
            self.x_coord = self.start_position_x
            self.y_coord = self.start_position_y
            self.teleport = False
        # update ship position
        self.rect.x = self.x_coord
        self.rect.y = self.y_coord
        

    def blitme(self):
        """drow ship at display"""
        self.screen.blit(self.image, self.rect)