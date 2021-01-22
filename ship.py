import pygame
class Ship():
    """Class for driving spaceship"""
    def __init__(self, ai_game):
        """initialization  starship and set it start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get rectangle.
        self.image = pygame.image.load('images/star_fury.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()
        # every new ship creates on bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """drow ship at display"""
        self.screen.blit(self.image, self.rect)