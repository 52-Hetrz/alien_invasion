import pygame
from settings import Settings
import game_functions as gf
from ship import Ship


def run_game():
    # 初始化屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption(settings.game_name)

    # 创建飞船对象
    ship = Ship(screen)
    while True:
        gf.check_events(ship)
        ship.update_position()
        gf.update_screen(screen, settings, ship)


run_game()