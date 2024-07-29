#第13步：优化过渡页面按钮使用空格键进行快捷操作

import pygame,sys
import birds2 as birds    
import pigs2 as pigs
screen=pygame.display.set_mode((600,337))
pygame.init()
pygame.mixer.init()
gatelevel=0 
game_gate=[
    {
        'bgimg':'src/image/bg.png','birdimg':'src/image/ab.png','pigimg':'src/image/pig.png','bgmusic':'src/music/Anger_Bird.mp3','movespeed':40
    },
    {
        'bgimg':'src/image/bg2.png','birdimg':'src/image/ab2.png','pigimg':'src/image/pig2.png','bgmusic':'src/music/funky_theme_2.mp3','movespeed':20
    }
    ]

def main():
    global gatelevel
    pygame.display.set_caption("愤怒的小鸟_开始界面")
    bg=pygame.image.load(game_gate[gatelevel]['bgimg'])
    bgpos=bg.get_rect()
    pygame.mixer.music.load(game_gate[gatelevel]['bgmusic'])
    pygame.mixer.music.set_volume(0.2) 
    pygame.mixer.music.play(loops=-1) 
    bird=birds.Bird(game_gate[gatelevel]['birdimg']) 
    group=pygame.sprite.Group() 
    i=0 
    state=True
    while state:
        screen.blit(bg,bgpos)
        screen.blit(bird.img,bird.rect) 
        
        if i%game_gate[gatelevel]['movespeed']==0:
            pig=pigs.Pig(game_gate[gatelevel]['pigimg'])
            group.add(pig)  
        i+=1    
        for p in group.sprites():
            p.move()
            screen.blit(p.img,p.rect)   
            if pygame.sprite.collide_rect(bird,p):
                state=False
                game_continue(0)

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
            state=False
            gatelevel+=1
            if gatelevel==len(game_gate):
                gatelevel=0 
                game_continue(2)
            else:
                game_continue(1)

def game_continue(ko):
    uitpye=[{'tips_bgimg':'src/image/gameover.png','tips_title':'愤怒的小鸟_游戏结束','tips_but':'src/image/restar.png','tips_but2':'src/image/restar2.png'},
            {'tips_bgimg':'src/image/bg2.png','tips_title':'愤怒的小鸟_恭喜，进入下一关','tips_but':'src/image/button.png','tips_but2':'src/image/button2.png'},
            {'tips_bgimg':'src/image/success.png','tips_title':'愤怒的小鸟_恭喜，通关成功','tips_but':'src/image/but_success.png','tips_but2':'src/image/but_success2.png'}
            ] 
    pygame.mixer.music.stop() 
    bg_go=pygame.image.load(uitpye[ko]['tips_bgimg'])
    pygame.display.set_caption(uitpye[ko]['tips_title'])
    bg_gopos=bg_go.get_rect()
    screen.blit(bg_go,bg_gopos)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        img=pygame.image.load(uitpye[ko]['tips_but'])
        img_srcpos=img.get_rect(center=(screen.get_width()/2,screen.get_height()/2+100))
        left=img_srcpos.left
        top=img_srcpos.top
        right=img_srcpos.right
        bottom=img_srcpos.bottom
        mouse_press=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos() 
        key=pygame.key.get_pressed()     #增加检测是否有按键盘的操作
        if left<=mouse_pos[0]<=right and top<=mouse_pos[1]<=bottom or key[pygame.K_SPACE]:  #增加用于判断是否按了“空格键”在按钮上
            img=pygame.image.load(uitpye[ko]['tips_but2'])
            img_srcpos=img.get_rect(center=(screen.get_width()/2,screen.get_height()/2+100))
            if mouse_press[0] or key[pygame.K_SPACE]:  #增加用于判断是否按了“空格键”在按钮上
                main()
        screen.blit(img,img_srcpos)
        pygame.display.update()
        pygame.time.Clock().tick(60)

main()