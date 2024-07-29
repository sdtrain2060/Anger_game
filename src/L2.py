#第02步：在主界面中加载一只小鸟【注意：绿色注释部分和birds.py是此文件程序与L1.py相比增加的部分】

import pygame,sys
import birds    #导入birds.py里自定义class类的模块。birds.py文件作用是定义小鸟的属性和动作
screen=pygame.display.set_mode((600,337))
pygame.init()
pygame.display.set_caption("愤怒的小鸟_开始界面")
bg=pygame.image.load("src/image/bg.png")
bgpos=bg.get_rect()
bird=birds.Bird()    #实例化Bird类，并赋值给bird，这样就可以在此文件程序里调用Bird类里的属性和动作了。
while True:
    screen.blit(bg,bgpos)
    screen.blit(bird.img,bird.rect)     #把birds.py文件里自定义的class类里img和rect属性值读取到此处，并在名为screen的窗口里绑定显示
    pygame.display.update()     #这里的update()是显示名为screen窗口里的所有内容，包括背景图、小鸟等
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()