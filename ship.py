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
        self.rect.centery = self.rect.bottom - size[1]/2

        # 设置飞船的移动速度
        self.speed = 1

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
        if self.right:
            self.rect.centerx += self.speed
        elif self.left:
            self.rect.centerx -= self.speed
        elif self.up:
            self.rect.centery -= self.speed
        elif self.down:
            self.rect.centery += self.speed
