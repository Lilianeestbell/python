class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)
        # self.screen_color = (176, 224, 230)

        #飞船的位置
        self.ship_speed_factor = 1.5
        #子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60,
        self.bullet_allowed = 3

class MySettings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.screen_color = (176, 224, 230)

