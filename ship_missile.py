import pygame
from pygame.sprite import Sprite
    
class ShipMissile(Sprite):
    """class for firing missile"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.max_on_display = 3
        self.missile_speed_per_sec = self.settings.missile_speed_per_sec
        self.missile_radius = 5
        self.missile_color = [0, 68, 255]
        self.circle_center_coord = list(ai_game.ship.rect.center)
        self.missile_y_position = float(self.circle_center_coord[1])
        
        

    def update(self):
        self.missile_y_position -= self.missile_speed_per_sec
        self.circle_center_coord[1]= self.missile_y_position
        

    def draw_missile (self):
        pygame.draw.circle(self.screen, self.missile_color,
                         self.circle_center_coord, self.missile_radius)
        