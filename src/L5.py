#第05步：在主界面中随机加入多只运动的猪，但未实现碰撞检测功能

import pygame,sys
import birds    
import pigs
screen=pygame.display.set_mode((600,337))
pygame.init()
pygame.display.set_caption("愤怒的小鸟_开始界面")
bg=pygame.image.load("src/image/bg.png")
bgpos=bg.get_rect()
bird=birds.Bird()    
group=pygame.sprite.Group() #创建一个精灵组，用于存放所有的猪;组的作用是方便统一遍历操作所有的猪对象
i=0 #计数器，用于控制猪的生成速度
while True:
    screen.blit(bg,bgpos)
    screen.blit(bird.img,bird.rect) 
    #if实现每循环30次就生成一只猪
    if i%30==0:
        pig=pigs.Pig()  #每调用一次pigs.py文件里的Pig()方法就实例化生成一只猪
        group.add(pig)  #将生成的猪对象添加到精灵组中
    i+=1    #每隔30次循环，就生成一只猪

    #遍历精灵组中的所有猪对象，并调用每只猪类里move()的方法,来移动猪的位置
    for p in group.sprites():   #此处的group.sprites()一定要配合“pigs.py”文件在自定义class类里需要继承pygame.sprites.Sprites的基础类才行正常运行，否则会出错。
        p.move()    #每遍历一只猪，就调用move()方法，来移动猪的位置
        screen.blit(p.img,p.rect)   #每遍历一只猪，就调用blit()方法，将猪绑定到screen屏幕上

    pygame.display.update() #当上面的背景图、小鸟、所有的猪等都绑定到屏幕上后，调用update()方法，将屏幕上的内容显示出来
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
