#第10步：改写游戏为通用型一关变成多关功能

import pygame,sys
import birds2 as birds    
import pigs2 as pigs
screen=pygame.display.set_mode((600,337))
pygame.init()
pygame.mixer.init()
gatelevel=0     #增加一个记录当前游戏是第几关，方便后面实现跳转到下一关指定具体关数
game_gate=[
    {
        'bgimg':'src/image/bg.png','birdimg':'src/image/ab.png','pigimg':'src/image/pig.png','bgmusic':'src/music/Anger_Bird.mp3','movespeed':40
    },
    {
        'bgimg':'src/image/bg2.png','birdimg':'src/image/ab2.png','pigimg':'src/image/pig2.png','bgmusic':'src/music/funky_theme_2.mp3','movespeed':20
    }
    ]

def main():
    global gatelevel    #引用自定义函数之外的全局变量，否则会报“无法调用”的错误提示
    pygame.display.set_caption("愤怒的小鸟_开始界面")
    bg=pygame.image.load(game_gate[gatelevel]['bgimg']) #实现变量动态调用
    bgpos=bg.get_rect()
    pygame.mixer.music.load(game_gate[gatelevel]['bgmusic']) #实现变量动态调用
    pygame.mixer.music.set_volume(0.2) 
    pygame.mixer.music.play(loops=-1) 
    bird=birds.Bird(game_gate[gatelevel]['birdimg'])     #实现变量动态调用
    group=pygame.sprite.Group() 
    i=0 
    state=True
    while state:
        screen.blit(bg,bgpos)
        screen.blit(bird.img,bird.rect) 
        
        if i%game_gate[gatelevel]['movespeed']==0:
            pig=pigs.Pig(game_gate[gatelevel]['pigimg'])  #实现变量动态调用
            group.add(pig)  
        i+=1    
        for p in group.sprites():
            p.move()
            screen.blit(p.img,p.rect)   
            if pygame.sprite.collide_rect(bird,p):
                state=False
                game_continue(0)     #增加一个调用形式参数，目的是指明是“游戏结束”而调用game_continue()函数，值为0

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
            game_continue(1)     #增加一个调用形式参数，目的是指明是“游戏进入下一关”而调用game_continue()函数，值为1

def game_continue(ko):
    #下面增加一个列表，用于存储本函数作为“游戏结束”和“游戏进入下一关”时的过渡提示页面中所需的相关内容信息，方便灵活显示处理
    uitpye=[{'tips_bgimg':'src/image/gameover.png','tips_title':'愤怒的小鸟_游戏结束','tips_but':'src/image/restar.png','tips_but2':'src/image/restar2.png'},
            {'tips_bgimg':'src/image/success.png','tips_title':'愤怒的小鸟_恭喜，进入下一关','tips_but':'src/image/button.png','tips_but2':'src/image/button2.png'}
            ]
    pygame.mixer.music.stop() 
    bg_go=pygame.image.load(uitpye[ko]['tips_bgimg'])   #通过调用uitpye列表来动态生成过渡页面内容
    pygame.display.set_caption(uitpye[ko]['tips_title'])  #通过调用uitpye列表来动态生成过渡页面内容
    bg_gopos=bg_go.get_rect()
    screen.blit(bg_go,bg_gopos)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        img=pygame.image.load(uitpye[ko]['tips_but'])  #通过调用uitpye列表来动态生成过渡页面内容
        img_srcpos=img.get_rect()
        left=img_srcpos.left
        top=img_srcpos.top
        right=img_srcpos.right
        bottom=img_srcpos.bottom
        mouse_press=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos() 
        if left<=mouse_pos[0]<=right and top<=mouse_pos[1]<=bottom: 
            img=pygame.image.load(uitpye[ko]['tips_but2'])    #通过调用uitpye列表来动态生成过渡页面内容
            img_srcpos=img.get_rect()
            if mouse_press[0]: 
                main()
        screen.blit(img,img_srcpos)
        pygame.display.update()
        pygame.time.Clock().tick(60)

main()