#第07步：实现成功通关，进入下一关游戏的功能

import pygame,sys
import birds    
import pigs
screen=pygame.display.set_mode((600,337))
pygame.init()
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
        
        if i%40==0:
            pig=pigs.Pig() 
            group.add(pig)  
        i+=1    
        for p in group.sprites():
            p.move()
            screen.blit(p.img,p.rect)   
            if pygame.sprite.collide_rect(bird,p):
                state=False
                game_continue()

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
        if bird.rect.right>=600:    #判断是否通关，并自动跳转到下一关
            game_next() #调用下一关游戏的函数

def game_continue():
    bg_go=pygame.image.load("src/image/gameover.png")
    pygame.display.set_caption("愤怒的小鸟_游戏结束")
    bg_gopos=bg_go.get_rect()
    screen.blit(bg_go,bg_gopos)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        img=pygame.image.load("src/image/restar.png")
        img_srcpos=img.get_rect()
        left=img_srcpos.left
        top=img_srcpos.top
        right=img_srcpos.right
        bottom=img_srcpos.bottom
        mouse_press=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos() 
        if left<=mouse_pos[0]<=right and top<=mouse_pos[1]<=bottom: 
            img=pygame.image.load("src/image/restar2.png")  
            img_srcpos=img.get_rect()
            if mouse_press[0]: 
                main()
        screen.blit(img,img_srcpos)
        pygame.display.update()
        pygame.time.Clock().tick(60)

#下面的函数是游戏通关，进入下一关的游戏功能
def game_next():
    print('恭喜进入下一关！')

main()