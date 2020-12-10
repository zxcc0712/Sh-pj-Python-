import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创造一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于储存子弹的编组
    bullets =Group()

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标的事件
        gf.check_events(ai_settings,screen,ship,bullets)

        ship.update()
        bullets.update()

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings,screen,ship,bullets)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()