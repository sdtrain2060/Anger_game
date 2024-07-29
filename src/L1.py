#第01步：此程序只实现显示游戏主界面功能

import pygame,sys   #引入界面游戏开发库和系统库
screen=pygame.display.set_mode((600,337))   #通过pygame库创建一个游戏窗口
pygame.init()   #初始化pygame库里的所有功能（属性、参数值）
pygame.display.set_caption("愤怒的小鸟_开始界面")   #为窗口设置标题
bg=pygame.image.load("src/image/bg.png")    #通过pygame库加载游戏背景图片，但还没有绑定到窗口上，更加没有显示出来
bgpos=bg.get_rect() #获取背景图片的矩形区域，为绑定到窗口做准备
while True: #实现窗口的循环显示，避免窗口一闪而过
    screen.blit(bg,bgpos)   #绑定背景图片到窗口上
    pygame.display.update() #刷新显示绑定在窗口上的背景图片
    pygame.time.Clock().tick(60)    #设置窗口刷新速度为60帧每秒
    for event in pygame.event.get():    #实现窗口的交互功能，比如鼠标单击来关闭窗口的操作。避鼠标无法操作窗口的关闭操作
        if event.type==pygame.QUIT:     #判断窗口操作是否为鼠标单击关闭窗口
            pygame.quit()   #退出pygame游戏功能
            sys.exit()  #退出整个程序，实现完全关闭窗口