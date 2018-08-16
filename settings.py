class Settings:
    """store settings"""

    def __init__(self):
        """init"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (90, 90, 90)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 215, 0
        self.bullets_allowed = 3

        # stars settings
        self.number_stars_x = 10
        self.number_stars_rows = 7

        # aliens settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # meteors settings
        self.meteors_allowed = 10
        self.meteor_speed_factor = 5

