import pygame
from pygame .sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from BackGround import Sign


def run_game():
    # init game, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # create a ship object
    ship = Ship(ai_settings, screen)
    sign = Sign(screen)
    # create a bullet group
    bullets = Group()
    # create an alien group
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stars = Group()
    gf.create_starry_night(ai_settings, screen, stars)
    meteors = Group()
    gf.create_meteors(ai_settings, screen, meteors)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, sign, stars)


run_game()
