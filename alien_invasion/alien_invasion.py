import sys

import pygame

from setting import Settings, MySettings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏，并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # my_settings = MySettings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 设置bg_colordraw_bullet
    # bg_color = ai_settings.screen_color
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, bullets, ship)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, bullets, ship)

run_game()
