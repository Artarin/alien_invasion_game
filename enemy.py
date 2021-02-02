import pygame
from pygame.sprite import Sprite

class EnemyShip(Sprite):
    """enemy object and it properties and behavior"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/enemy_ship_1_2.png').convert()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x_position = float(self.rect.x)
        self.settings = ai_game.settings
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return  True    

    def update(self):
        # print (self.rect.x )
        self.x_position = self.rect.x
        self.x_position +=  self.settings.enemy_x_speed * self.settings.enemy_direction
        self.rect.x = int(self.x_position)

    