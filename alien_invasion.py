import pygame
import settings
import sys


def run_game():
    # 初始化屏幕对象
    pygame.init()
    game_settings = settings.Settings()
    screen = pygame.display.set_mode(game_settings.screen_size)
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(game_settings.bg_color)
        pygame.display.flip()


run_game()