"""
@Project    ：alien_invasion
@File       ：game_functions.py
@Description：游戏的辅助函数文件
@Author     ：Life
@Date       ：2021/4/2
"""

import pygame
import sys
from alien import Alien


def check_keyup_events(event, ship):
    """监测键盘弹起事件
    :param event: 键盘事件
    :param ship: 飞船
    """
    # 根据弹起的按键更新飞船的移动状态
    if event.key == pygame.K_d:
        ship.right = False
    elif event.key == pygame.K_a:
        ship.left = False
    elif event.key == pygame.K_w:
        ship.up = False
    elif event.key == pygame.K_s:
        ship.down = False


def check_keydown_events(event, ship, bullets, settings):
    """监测键盘按下事件
    :param settings:  游戏基本设置
    :param event：    键盘事件
    :param ship：     飞船
    :param bullets：  子弹集合列表
    """
    # 根据按下的按键更新飞船的移动状态
    if event.key == pygame.K_d:
        ship.right = True
    elif event.key == pygame.K_a:
        ship.left = True
    elif event.key == pygame.K_w:
        ship.up = True
    elif event.key == pygame.K_s:
        ship.down = True
    elif event.key == pygame.K_SPACE and len(bullets) < settings.bullets_allowed:
        new_bullet = ship.shoot()
        bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(ship, bullets, settings):
    """监测键盘和鼠标事件
    :param settings: 游戏基本设置
    :param ship: 飞船
    :param bullets: 子弹的集合列表
    """
    for event in pygame.event.get():
        # 点击关闭按钮
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(screen, screen_settings, ship, bullets, alien):
    """更新屏幕
    :param alien: 需要绘制的外星人
    :param screen: 需要更新的屏幕
    :param screen_settings: 屏幕设置参数
    :param ship: 需要在屏幕上绘制的飞船
    :param bullets: 子弹的集合列表
    """
    screen.fill(screen_settings.bg_color)
    ship.blit_me()
    alien.blit_me()
    for bullet in bullets:
        bullet.draw_bullet()
    pygame.display.flip()


def creat_fleet(settings, screen, aliens):
    """
    创建外星人群，并检测一行能容纳多少个外星人
    :param screen: 创建外星人的屏幕
    :param aliens: 外星人组
    :param settings: 系统设置
    :return:
    """
    alien = Alien(screen)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    for alien_number in range(number_aliens_x):
        alien = Alien(screen)
        alien_x = alien_width + alien_width * 2 * alien_number
        alien.rect.x = alien_x
        aliens.add(alien)
