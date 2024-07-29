#第06步：实现重玩一次按钮单击后重新开始游戏的功能

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
        #下面四句是获得restar重玩按钮的位置数，后面用来与鼠标的位置进行位置是否重叠判断，实现鼠标单击和鼠标经过的功能处理的准备
        left=img_srcpos.left
        top=img_srcpos.top
        right=img_srcpos.right
        bottom=img_srcpos.bottom
        #下面两句是获得鼠标单击和单击时的位置数
        mouse_press=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()    #mouse_pos[0]表示水平方向X坐标的鼠标位置；mouse_pos[1]表示垂直方向Y坐标的鼠标位置
        if left<=mouse_pos[0]<=right and top<=mouse_pos[1]<=bottom: #通过鼠标位置数与restar图片位置数的范围比较来判断鼠标是否落在restar位置上
            #以下两句实现鼠标经过restar位置时，重玩按钮会变颜色的效果
            img=pygame.image.load("src/image/restar2.png")  
            img_srcpos=img.get_rect()
            if mouse_press[0]:  #mouse_press[0]为True或者1时表示鼠标单击动作发生
                main()  #调用游戏的主界面，重新玩游戏
        screen.blit(img,img_srcpos)
        pygame.display.update()
        pygame.time.Clock().tick(60)

main()