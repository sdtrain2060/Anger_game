#第06步：实现小鸟与猪的碰撞后显示重玩一次按钮的功能

import pygame,sys
import birds    
import pigs
screen=pygame.display.set_mode((600,337))
pygame.init()

#将下面的代码块打包成一个函数，用于实现游戏结束后的可以重新从头开始的功能
def main():
    pygame.display.set_caption("愤怒的小鸟_开始界面")
    bg=pygame.image.load("src/image/bg.png")
    bgpos=bg.get_rect()
    bird=birds.Bird()    
    group=pygame.sprite.Group() 
    i=0 
    state=True
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
                state=False
                game_continue() #调用碰撞后显示游戏结束和显示重玩一次按钮的函数

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

#以下函数实现碰撞后游戏结束的提示界面和显示重玩一次按钮
def game_continue():
    bg_go=pygame.image.load("src/image/gameover.png")   #加载“游戏结束”的提示图片
    pygame.display.set_caption("愤怒的小鸟_游戏结束")
    bg_gopos=bg_go.get_rect()
    screen.blit(bg_go,bg_gopos)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        img=pygame.image.load("src/image/restar.png")   #加载“重玩”按钮的图片
        img_srcpos=img.get_rect()
        screen.blit(img,img_srcpos)
        pygame.display.update()
        pygame.time.Clock().tick(60)

main()