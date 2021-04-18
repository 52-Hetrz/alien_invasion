"""
@Project    ：alien_invasion
@File       ：alien_invasion.py
@Description：游戏的运行逻辑部分
@Author     ：Life
@Date       ：2021/4/1
"""

import pygame
from settings import Settings
import game_functions as gf
from ship import Ship
from alien import Alien
from pygame.sprite import Group


def run_game():
    # 初始化屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption(settings.game_name)

    # 创建飞船对象
    ship = Ship(screen)

    # 创建外星人对象
    alien = Alien(screen)

    # 创建子弹的集合列表
    bullets = Group()

    # 创建外星人集合
    aliens = Group()
    while True:
        gf.check_events(ship, bullets, settings)
        ship.update_position()
        bullets.update()
        alien.update()
        gf.update_screen(screen, settings, ship, bullets, alien)

        # 删除超出屏幕的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)


run_game()
