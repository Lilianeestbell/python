import sys

import pygame
from bullet import Bullet

def fire_bullets(event, ai_setting, screen, bullets, ship):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

#监听事件类型
def check_keydown_events(event, ai_setting, screen, bullets, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_bottom = True
    elif event.key == pygame.K_DOWN:
        ship.moving_top = True
    # 一定要写明白是event.key or event.type
    elif event.key == pygame.K_SPACE:
        fire_bullets(event, ai_setting, screen, bullets, ship)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_bottom = False
    elif event.key == pygame.K_DOWN:
        ship.moving_top = False

def check_events(ai_setting, screen, bullets, ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, bullets, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # 如果要改成让飞船停在屏幕左边 if bullet.rect.right >= 1200:bullets.remove(bullet)
    print(len(bullets))

#更新屏幕
def update_screen(ai_setting, screen, bullets, ship):
    #更新屏幕上的图像，并且切换到新屏幕
    #每次循环的时候都重绘屏幕
    screen.fill(ai_setting.screen_color)
    #重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet() 
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()
