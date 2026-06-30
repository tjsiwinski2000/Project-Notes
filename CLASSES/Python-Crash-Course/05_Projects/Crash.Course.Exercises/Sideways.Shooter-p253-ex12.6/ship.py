import pygame

class Ship:
    """ A class to manage the ship """
    
    def __init__(self, ai_game):
        """ initialize the ship and its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom left of the screen.
        self.rect.bottomleft = self.screen_rect.bottomleft
        
        # Store a float for the ship's exact horizontal position.
        self.y = float(self.rect.y)
        
        # Movement flag; start with a ship that's not moving.
        self.moving_up= False
        self.moving_down = False
        
    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Update the ship's position based on the movement flag. """
        # Update the ship's x value, not the rect.
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
            # print(f"{self.rect.right} : {self.screen_rect.right}")
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            # print(f"{self.rect.left}")
        #Update rect object from self.x.
        self.rect.y = self.y