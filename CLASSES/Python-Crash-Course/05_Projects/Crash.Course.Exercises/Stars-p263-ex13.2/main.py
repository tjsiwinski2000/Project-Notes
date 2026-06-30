import pygame
from pygame.sprite import Sprite
from star import Star
import sys

# create a pygame screen
class StarrySky:
    """Overall class to manage dispay and behaviour"""
    def __init__(self):
        pygame.init()
        self.screen= pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Starry Night")
        #self.star = Star(self)
        self.stars = pygame.sprite.Group()
        self._create_many_stars()
        

    def run_sky(self):
        while True:
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit()
                    
    def _create_many_stars(self):
        # Create a star and keep adding them [until no room]
        star = Star(self)
        self.stars.add(star)
        print(star.x)
        new_star = Star(self)
        new_star.x = star.x + star.rect.x *10
        print(new_star.x)
        self.stars.add(new_star)
        self.stars.draw(self.screen)
        # star_width = star.rect.width
        # current_x = star_width
        # while current_x < (self.screen_width -2 * star_width):
        #     new_star = Star(self)
        #     new_star.x = current_x
        #     new_star.rect.x = current_x
        #     self.stars.add(new_star)
        #     current_x +- 2 *star_width
            
   
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ssky = StarrySky()
    ssky.run_sky()
            
# create helper _draw_star

# create helper _draw_star_row
# regroup and fill screen with starts