import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a administrate class of bullet which fired by ship"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # build a bullet at (0, 0) of screen
        # then set it to the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet position by float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """raise the bullet"""
        # update the float of bullet position
        self.y -= self.speed_factor
        # update the rect of bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

