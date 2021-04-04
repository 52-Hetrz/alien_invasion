"""
@Project    ：alien_invasion
@File       ：ship.py
@Description：函数的飞船文件
@Author     ：Life
@Date       ：2021/4/2
"""

import pygame


class Ship:
    def __init__(self, screen):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 获取飞船的图像，及其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        size = self.rect.size

        # 设置飞船的中心坐标
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.rect.bottom - size[1] / 2

        # 设置飞船的移动速度
        self.speed = 2
        self.move_condition = 0

        # 设置飞船的移动参数
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def blit_me(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        """更新飞船的位置"""
        self.move_condition = self.count_move_condition()
        if not self.move_condition:
            if self.right and self.check_right_margin():
                self.rect.centerx += 1
            elif self.left and self.check_left_margin():
                self.rect.centerx -= 1
            elif self.up and self.check_top_margin():
                self.rect.centery -= 1
            elif self.down and self.check_bottom_margin():
                self.rect.centery += 1

    def check_top_margin(self):
        """飞船的上边界有效域检测函数"""
        if self.rect.top <= self.screen_rect.top:
            return False
        return True

    def check_bottom_margin(self):
        """飞船的下边界有效域检测函数"""
        if self.rect.bottom >= self.screen_rect.bottom:
            return False
        return True

    def check_left_margin(self):
        """飞船的左边界有效域检测函数"""
        if self.rect.left <= self.screen_rect.left:
            return False
        return True

    def check_right_margin(self):
        """飞船的右边界有效域检测函数"""
        if self.rect.right >= self.screen_rect.right:
            return False
        return True

    def count_move_condition(self):
        """根据move_condition和speed计算下一个move_condition的值"""
        return (self.move_condition + 1) % (7 - self.speed)
