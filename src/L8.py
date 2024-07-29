#第08步：为游戏加入背景音乐

import pygame,sys
import birds    
import pigs
screen=pygame.display.set_mode((600,337))
pygame.init()
pygame.mixer.init() #初始化音乐功能模块
def main():
    pygame.display.set_caption("愤怒的小鸟_开始界面")
    bg=pygame.image.load("src/image/bg.png")
    bgpos=bg.get_rect()
    pygame.mixer.music.load('src/music/Anger_Bird.mp3') #加载背景音乐到游戏
    pygame.mixer.music.set_volume(0.2)  #设置背景音乐音量值，值的范围为0~1
    pygame.mixer.music.play(loops=-1)   #设置播放次数，-1表示循环播放
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
        if bird.rect.right>=600: 
            game_next() 

def game_continue():
    pygame.mixer.music.stop()   #当游戏结束时，游戏背景音乐停止
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

def game_next():
    print('恭喜进入下一关！')

main()