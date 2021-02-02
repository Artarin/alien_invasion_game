import pygame
from random import randint

class Settings():
    """class for saving all serrings game alien invasion"""

    def __init__(self, ai_game):
        self.background = pygame.image.load('images/space.jpg')
        self.bg_color = (0, 0, 0)
        self.max_fps = 60
        self.delta_time_ms = 1000 / self.max_fps
        self.clock = pygame.time.Clock()
        self.old_time = pygame.time.get_ticks()
        self.milliseconds_counter = 0
        self.fps_counter = 0
        self.returned_fps = 0
        self.ship_speed_per_sec = 1000
        self.missile_speed_per_sec = (self.ship_speed_per_sec+200)/self.max_fps
        self.enemy_x_speed = (self.ship_speed_per_sec /2) / self.max_fps
        self.enemy_y_speed = (self.ship_speed_per_sec ) / self.max_fps
        self.enemy_direction = 1
        pygame.mixer.music.load('audio/main.mp3')
        pygame.mixer.music.play(-1)
        self.ship_blast = pygame.mixer.Sound('audio/laser_blast.mp3')
        self.enemy_destroy = pygame.mixer.Sound('audio/enemy_destroy.mp3')
    
    


    def fps_controller(self, ai_game):
        self.clock.tick(self.max_fps)
                
        # font = pygame.font.Font(None, 25)
        # fps = self.clock.get_fps()
        # self.fps_overlay = font.render(str(int(fps)), True, (254,254,254))
        # return (self.fps_overlay)
        # i have pygame fps func, but interested to write my own:
        self.new_time = pygame.time.get_ticks()
        self.delta_time_ms = self.new_time - self.old_time
        self.old_time = self.new_time
        self.milliseconds_counter += self.delta_time_ms
        self.fps_counter += 1
        if self.milliseconds_counter >= 1000:
            self.milliseconds_counter -= 1000
            self.returned_fps = self.fps_counter
            self.fps_counter = 0
        font = pygame.font.Font(None, 25)
        self.fps_overlay = font.render(str(int(self.returned_fps)), True, (254,254,254))
        return (self.fps_overlay)

