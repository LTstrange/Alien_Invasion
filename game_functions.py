import sys
import pygame
import random
from bullet import Bullet
from alien import Alien
from BackGround import Stars, Meteor


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond the key_down"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_d:
        # fly to right
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """respond the key_up"""
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):

    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets, sign, stars, meteors):
    """update the image in the screen and change to the newer screen"""
    # flash screen every loop
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    create_meteors(ai_settings, screen, meteors)
    meteors.draw(screen)
    sign.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(aliens, bullets):
    """update the bullets' position and delete the fade bullets"""
    # update the bullets' position
    bullets.update()

    # delete the bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for collisions between bullets and aliens
    # If so, remove the corresponding bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def get_number_aliens_x(ai_settings, alien_width):
    """compute how many aliens can be accommodated"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """compute how many rows of alien can be accommodated"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien,  and then add to the line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """create alien's group"""
    # alien's width is alien's interval
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    # create the first line of aliens
    for row_number in range(number_rows - 1):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


def create_star(ai_settings, screen, number_stars_x, number_stars_rows, star_number, row_number, stars):
    star = Stars(screen)
    star.rect.x = ((ai_settings.screen_width / number_stars_x) * star_number +
                   random.randint(1, int((ai_settings.screen_width / number_stars_x))))
    star.rect.y = ((ai_settings.screen_height / number_stars_rows) * row_number +
                   random.randint(1, int((ai_settings.screen_height / number_stars_rows))))
    stars.add(star)


def create_starry_night(ai_settings, screen, stars):
    number_stars_x = ai_settings.number_stars_x
    number_stars_rows = ai_settings.number_stars_rows

    for row_number in range(number_stars_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, number_stars_x, number_stars_rows, star_number, row_number, stars)


def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def check_fleet_edges(ai_settings, aliens):
    """take actions when fleet reach edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """move down the hole fleet and change direction of then"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def create_meteors(ai_settings, screen, meteors):
    if rand_num_meteors() and (len(meteors.copy()) <= ai_settings.meteors_allowed):
        meteor = Meteor(screen, ai_settings)
        meteor.rect.x = random.randint(0, ai_settings.screen_width - meteor.rect.width)
        meteors.add(meteor)


def rand_num_meteors():
    if random.randint(0, 50) == 0:
        return True


def update_meteors(ai_settings, meteors):
    meteors.update()

    for meteor in meteors.copy():
        if meteor.rect.y >= ai_settings.screen_height:
            meteors.remove(meteor)

