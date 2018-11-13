import pygame
from pygame.locals import *
# import time


def main():
    """程序的主逻辑"""
    screen = pygame.display.set_mode((480, 700), 0, 32)

    # 创建背景图片
    bg = pygame.image.load('./feiji/background.png')

    # 创建玩家飞机图片
    hero = pygame.image.load('./feiji/hero.gif')
    heroX = 190
    heroY = 520

    while True:
        # 显示背景图片
        screen.blit(bg, (0, 0))

        # 显示玩家飞机
        screen.blit(hero, (heroX, heroY))

        # 获取事件，比如按键等
        for event in pygame.event.get():
            # 判断是否点击了退出按钮
            if event.type == QUIT:
                print('exit')
                exit()
            # 判断是否按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a 或者 left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    heroX -= 10
                    if heroX <= 0:
                        heroX = 0
                # 检测按键是否是d 或者 right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    heroX += 10
                    if heroX >= 380:
                        heroX = 380
                # 检测按键是否是空格
                elif event.key == K_SPACE:
                    print('space')

        # 刷新界面
        pygame.display.update()

        # time.sleep(10)


if __name__ == '__main__':
    print('程序开始')
    main()
    print('程序结束')
