import pygame
from pygame.sprite import Sprite


class Sign:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('image/sign (2).png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = 10
        self.rect.y = 10

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Stars(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('image/star1.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Meteor(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('image/meteor.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.ai_settings.meteor_speed_factor
        self.rect.y = self.y

