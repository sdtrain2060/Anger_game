#第06步：实现小鸟与猪的碰撞后游戏界面退出，但未能实现重新再来一局的功能

import pygame,sys
import birds    
import pigs
screen=pygame.display.set_mode((600,337))
pygame.init()
pygame.display.set_caption("愤怒的小鸟_开始界面")
bg=pygame.image.load("src/image/bg.png")
bgpos=bg.get_rect()
bird=birds.Bird()    
group=pygame.sprite.Group() 
i=0 
state=True  #用来控制游戏是否结束
while state:
    screen.blit(bg,bgpos)
    screen.blit(bird.img,bird.rect) 
    
    if i%30==0:
        pig=pigs.Pig() 
        group.add(pig)  
    i+=1    
    for p in group.sprites():
        p.move()    
        screen.blit(p.img,p.rect)   
        if pygame.sprite.collide_rect(bird,p):
            state=False #实现游戏结束
            print("碰撞了")

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
