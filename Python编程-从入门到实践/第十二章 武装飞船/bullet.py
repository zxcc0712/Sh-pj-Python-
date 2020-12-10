import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射子弹进行管理的类'''

    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen

        # 在（0，0）处创建一个表示子弹形状的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.buttle_width,
                                ai_settings.buttle_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.colour = ai_settings.buttle_colour
        self.speed_factor = ai_settings.buttle_speed_factor

    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的小数值
        self.y -=self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.colour,self.rect)