import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """init ship and set the position when the game start"""
        self.screen = screen
        self.ai_settings = ai_settings

        # import ship's image and get it's rect
        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set the ship on the bottom & center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store the float number in the ship's attribute center
        self.FloatCenterX = float(self.rect.centerx)
        self.FloatBottom = float(self.rect.bottom)

        # the flag of moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """according the moving flag to change the ship's rect"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.FloatCenterX += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.FloatCenterX -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.FloatBottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.FloatBottom += self.ai_settings.ship_speed_factor

        # according the center update the rect
        self.rect.centerx = self.FloatCenterX
        self.rect.bottom = self.FloatBottom

    def center_ship(self):
        self.FloatCenterX = self.screen_rect.centerx
        self.FloatBottom = self.screen_rect.bottom

    def blitme(self):
        """bilt the ship at the position"""
        self.screen.blit(self.image, self.rect)

