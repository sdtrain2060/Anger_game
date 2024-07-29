#第04步：在主界面中加入一只小猪和让小猪自动随机无规律的运动起来

import pygame,sys
import birds    
import pigs     #引入pigs.py文件中小猪的类模块
screen=pygame.display.set_mode((600,337))
pygame.init()
pygame.display.set_caption("愤怒的小鸟_开始界面")
bg=pygame.image.load("src/image/bg.png")
bgpos=bg.get_rect()
bird=birds.Bird()    
pig= pigs.Pig()     #创建小猪的实例化对象
while True:
    screen.blit(bg,bgpos)
    screen.blit(bird.img,bird.rect) 
    screen.blit(pig.img,pig.rect)       #在主界面中绑定小猪图片和显示位置
    pygame.display.update()
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        bird.move_right()
    elif key[pygame.K_LEFT]: 
        bird.move_left()
    if key[pygame.K_UP]:
        bird.move_up()
    elif key[pygame.K_DOWN]:
        bird.move_down()
    pig.move()      #调用小猪类里的移动方法，实现移动小猪位置