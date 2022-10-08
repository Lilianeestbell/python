import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_setting, screen, ship):
        super().__init__()
        self.screen = screen
        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        # 如果要改成让飞船停在屏幕左边，子弹从右侧发出沿着x方向
        # self.rect = pygame.Rect(0, 0, ai_setting.bullet_height,  ai_setting.bullet_width)
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        # 如果要改成让飞船停在屏幕左边，子弹从右侧发出沿着x方向
        # self.rect.top = ship.rect.top + 20
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        # 如果要改成让飞船停在屏幕左边，子弹从右侧发出沿着x方向
        # self.x = float(self.rect.x)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):

        self.y -= self.speed_factor
        self.rect.y = self.y
        # 如果要改成让飞船停在屏幕左边，子弹从右侧发出沿着x方向
        # self.x += self.speed_factor
        # self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
