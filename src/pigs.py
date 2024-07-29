#这是配合L4.py的程序所新增的一个pigs猪类文件

import pygame
from random import randint  #引入随机数功能模块，为小猪出现的随机位置和每只猪的运动的随机速度做准备
class Pig(pygame.sprite.Sprite):    #在（）里一定要继承pygame库包里的系统精灵组类pygame.sprite.Sprite才行，否则在主程序L5.py及后面的所有使用此类的.py文件都会在运行时报错
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self) #初始化pygame.sprite.Sprite基础类的属性和常量值
        position=[600, randint(40, 337)]
        self.img= pygame.image.load('src/image/pig.png')
        self.rect = self.img.get_rect(center=position)
        self.speed= [-randint(1, 3),0]  #让每只猪的速度随机

    def move(self):
        self.rect=self.rect.move(self.speed)