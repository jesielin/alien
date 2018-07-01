import pygame

from alien import Alien
from settings import Settings
from ship import Ship
from pygame.sprite import Group

import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建存储子弹的编组
    bullets = Group()


    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建外星人
    aliens = Group()
    ship = Ship(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        gf.update_bullets(bullets)
        print(aliens)
        gf.update_aliens(aliens)

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
