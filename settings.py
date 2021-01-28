import pygame
class Settings():
    """class for saving all serrings game alien invasion"""

    def __init__(self, ai_game):
        """game settings initialization"""
        #screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (14, 7, 57)
        #fps settings
        self.max_fps = 60
        self.clock = pygame.time.Clock()
        self.old_time = pygame.time.get_ticks()
        self.milliseconds_counter = 0
        self.fps_counter = 0
        self.returned_fps = 0
        # ship settings
        self.begin_speed = 10.5
        self.ship_speed = self.begin_speed
        
       
            
    def fps_controller(self, ai_game):
        """ give a pause in game cycle, then it work too fast and returns fps object"""
        self.clock.tick(self.max_fps)
        
        
        # font = pygame.font.Font(None, 25)
        # fps = self.clock.get_fps()
        # self.fps_overlay = font.render(str(int(fps)), True, (254,254,254))
        # return (self.fps_overlay)
        # i have pygame fps func, but interested to write my own
        self.new_time = pygame.time.get_ticks()
        self.delta_time = self.new_time - self.old_time
        self.old_time = self.new_time
        self.milliseconds_counter += self.delta_time
        self.fps_counter += 1
        if self.milliseconds_counter >= 1000:
            self.milliseconds_counter -= 1000
            self.returned_fps = self.fps_counter
            self.fps_counter = 0
        font = pygame.font.Font(None, 25)
        self.fps_overlay = font.render(str(int(self.returned_fps)), True, (254,254,254))
        return (self.fps_overlay)

    def ship_speed_controller(self):
        """ up or down ship speed with the fps"""
        self.ship_speed = round(self.begin_speed*(self.delta_time/16.67), 2)
        print (self.delta_time, self.ship_speed)
        # if self.returned_fps !=0:
        #     self.ship_speed =self.begin_speed * self.returned_fps / self.max_fps