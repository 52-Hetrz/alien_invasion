"""
@Project    ：alien_invasion
@File       ：game_functions.py
@Description：游戏的辅助函数文件
@Author     ：Life
@Date       ：2021/4/2
"""

import pygame
import sys


def check_events(ship):
    """监测鼠标和键盘响应事件"""

    for event in pygame.event.get():
        # 点击关闭按钮
        if event.type == pygame.QUIT:
            sys.exit()

        # 飞船的操作部分
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.right = True
            elif event.key == pygame.K_a:
                ship.left = True
            elif event.key == pygame.K_w:
                ship.up = True
            elif event.key == pygame.K_s:
                ship.down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.right = False
            elif event.key == pygame.K_a:
                ship.left = False
            elif event.key == pygame.K_w:
                ship.up = False
            elif event.key == pygame.K_s:
                ship.down = False


def update_screen(screen, screen_settings, ship):
    """
    更新屏幕

    :param screen: 需要更新的屏幕
    :param screen_settings: 屏幕设置参数
    :param ship: 需要在屏幕上绘制的飞船
    :return:
    """
    screen.fill(screen_settings.bg_color)
    ship.blit_me()
    pygame.display.flip()
