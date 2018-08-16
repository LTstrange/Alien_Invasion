import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """describe the single alien's class"""

    def __init__(self, ai_settings, screen):
        """init the alien and set the start position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien's image and set it rect
        self.image = pygame.image.load('image/alien.png')
        self.rect = self.image.get_rect()

        # set the initial position around the screen's upper left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's accurate position
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move right aliens"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

#    def blitme(self):
#        self.screen.blit(self.image, self.rect)

