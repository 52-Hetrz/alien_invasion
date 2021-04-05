"""
@Project    ：alien_invasion 
@File       ：bullet.py
@Description：控制子弹的文件
@Author     ：Life
@Date       ：2021/4/4 11:08 
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen

        # 设置子弹的尺寸和颜色
        self.width = 3
        self.height = 15
        self.color = 60, 60, 60

        # 设置子弹的移动速度参数
        self.speed = 3
        self.move_condition = 0

        # 设置子弹的位置
        self.rect = pygame.Rect(0, 0, self.width, self.width)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    def update(self):
        """更新子弹的位置"""
        self.move_condition = self.count_move_condition()
        if not self.move_condition:
            self.rect.y -= 1

    def draw_bullet(self):
        """在屏幕上绘制子弹图像"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def count_move_condition(self):
        """根据move_condition和speed计算下一个move_condition的值"""
        return (self.move_condition + 1) % (7 - self.speed)



