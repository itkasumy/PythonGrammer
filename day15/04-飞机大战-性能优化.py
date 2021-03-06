import pygame
from pygame.locals import *
import time


class HeroPlane(object):

    def __init__(self, screen):
        # 飞机坐标
        self.x = 190
        self.y = 520
        # 显示的图片
        self.imagePath = './feiji/hero.gif'
        self.image = pygame.image.load(self.imagePath)
        # 显示窗口
        self.screen = screen
        self.moveStep = 15

        # 子弹的列表
        self.bullets = []

    def display(self):
        # 显示飞机
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.display()
            bullet.move()

    def moveLeft(self):
        self.x -= self.moveStep
        if self.x <= 0:
            self.x = 0

    def moveRight(self):
        self.x += self.moveStep
        if self.x >= 380:
            self.x = 380

    def shoot(self):
        # 发射一颗子弹
        bullet = Bullet(self.x, self.y, self.screen)
        self.bullets.append(bullet)

class Bullet(object):

    def __init__(self, planeX, planeY, screen):
        # 子弹的坐标
        self.x = planeX + 40
        self.y = planeY - 22

        # 子弹的图片
        self.imagePath = './feiji/bullet.png'
        self.image = pygame.image.load(self.imagePath)

        # 显示窗口
        self.screen = screen

    def display(self):
        # 显示子弹
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5


def main():
    """程序的主逻辑"""
    screen = pygame.display.set_mode((480, 700), 0, 32)

    # 创建背景图片
    bg = pygame.image.load('./feiji/background.png')

    # 创建玩家飞机
    hero = HeroPlane(screen)

    bullet = Bullet(hero.x, hero.y, screen)

    while True:
        # 显示背景图片
        screen.blit(bg, (0, 0))

        # 显示玩家飞机
        hero.display()
        # bullet.display()

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
                    hero.moveLeft()
                # 检测按键是否是d 或者 right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    hero.moveRight()
                # 检测按键是否是空格
                elif event.key == K_SPACE:
                    print('space')
                    hero.shoot()

        # 刷新界面
        pygame.display.update()

        time.sleep(1 / 100)


if __name__ == '__main__':
    print('程序开始')
    main()
    print('程序结束')
