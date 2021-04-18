"""
@Project    ：alien_invasion 
@File       ：alien.py
@Description：Alien Class
@Author     ：Life
@Date       ：2021/4/17 10:37 
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen

        # 加载图片
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 设置外星人的初始坐标
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 设置外星人的移动速度
        self.speed = 1
        self.move_condition = 0

        self.x = float(self.rect.x)

    def update(self):
        """
        更新外星人的位置坐标
        :return:
        """
        self.move_condition = self.count_move_condition()
        if self.move_condition == 0:
            self.rect.y += 1

    def blit_me(self):
        """
        绘制外星人
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def count_move_condition(self):
        """
        计算移动情况
        :return: 计算后的移动状态
        """
        return (self.move_condition + 1) % (20 - self.speed)
