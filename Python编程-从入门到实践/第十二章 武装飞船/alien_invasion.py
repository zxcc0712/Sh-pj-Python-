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

    # 创造一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets =Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标的事件
        gf.check_events(ai_settings,screen,ship,bullets)

        ship.update()
        gf.update_bullets(aliens,bullets)
        gf.update_aliens(ai_settings,aliens)

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()