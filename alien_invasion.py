import pygame
from pygame .sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
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

    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于储存统计信息的实例
    stats = GameStats(ai_settings)

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

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens,
                             bullets)
        gf.update_meteors(ai_settings, meteors)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets,
                         sign, stars, meteors, play_button, stats)


run_game()
