#这是配合L9.py的程序所新增的一个pigs猪类文件

import pygame
from random import randint 
class Pig(pygame.sprite.Sprite): 
    def __init__(self,pigimg) -> None:  #增加一个pigimg形式参数，用于接收从主程序传过来的小猪图片路径值，实现每关的小猪都不一样
        pygame.sprite.Sprite.__init__(self) 
        position=[600, randint(40, 337)]
        self.img= pygame.image.load(pigimg)
        self.rect = self.img.get_rect(center=position)
        self.speed= [-randint(1, 3),0] 

    def move(self):
        self.rect=self.rect.move(self.speed)