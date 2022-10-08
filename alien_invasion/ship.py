import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_setting = ai_settings
        # self.image = pygame.image.load('alien_invasion/images/panda.jpeg')
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #  如果要改成让飞船停在屏幕左边 self.rect.top = 376 self.rect.left = 0
        #在飞船的属性center中存储小数，因为centerx只能存储整数值
        self.center = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
            #更新飞船的center值，而不是更新react值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        if self.moving_top and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += self.ai_setting.ship_speed_factor
        if self.moving_bottom and self.rect.top > 0:
            self.centerY -= self.ai_setting.ship_speed_factor

        # 相当于定义一个新的变量进行一下数据处理，然后再把处理后的值赋给self.rect.centerx
        self.rect.centerx = self.center
        self.rect.centery = self.centerY

    def blitme(self):
        self.screen.blit(self.image, self.rect)
