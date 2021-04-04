"""
@Project    ：alien_invasion
@File       ：settings.py
@Description：游戏的参数设置文件
@Author     ：Life
@Date       ：2021/4/1
"""


class Settings:

    def __init__(self):
        """初始化游戏设置"""
        # 设定屏幕的基本参数
        self.screen_width = 960
        self.screen_height = 540
        self.bg_color = (230, 230, 230)
        self.screen_size = (self.screen_width, self.screen_height)
        self.game_name = "Alien Invasion"
