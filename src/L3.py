#第03步：在主界面中让小鸟在键盘的控制下运动起来

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
    key=pygame.key.get_pressed()    #获取键盘按键状态，并赋值给key
    if key[pygame.K_RIGHT]: #pygame.K_RIGHT是键盘上的右箭头键，key[pygame.K_RIGHT]是判断右箭头键是否被按下
        bird.move_right()   #调用Bird类里的move_right()方法，让小鸟向右移动
    elif key[pygame.K_LEFT]:    #pygame.K_LEFT是键盘上的左箭头键，key[pygame.K_LEFT]是判断左箭头键是否被按下
        bird.move_left()    #调用Bird类里的move_left()方法，让小鸟向左移动
    if key[pygame.K_UP]:    #pygame.K_UP是键盘上的上箭头键，key[pygame.K_UP]是判断上箭头键是否被按下
        bird.move_up()  #调用 Bird类里的move_up()方法，让小鸟向上移动
    elif key[pygame.K_DOWN]:    #pygame.K_DOWN是键盘上的下箭头键，key[pygame.K_DOWN]是判断下箭头键是否被按下
        bird.move_down()    #调用 Bird类里的move_down()方法，让小鸟向下移动