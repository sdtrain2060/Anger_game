import pygame
class Bird():   #【注意：此class里是没有继承pygame.sprite.Sprite的精灵基础类】
    def __init__(self) -> None:
        position=100,130    #此变量为类里的自定义局部变量，也不属于类的属性。100和130是经过人为制定的小鸟显示初始位置
        self.img=pygame.image.load("src/image/ab.png")  #为此类自定义一个名为img属性，“img”名字可以随意改成其它
        self.rect=self.img.get_rect(center=position)    #为此类自定义一个名为rect属性，“rect”名字可以随意改成其它



#以下的代码是为了配合L3.py文件程序而新增加的小鸟运动控制部分
    def move_right(self):
        self.speed=[2,0]
        if self.rect.right>=600:
            self.rect.right=600
        else:
            self.rect=self.rect.move(self.speed)    #一定要把move移动后的rect值重新赋值给self.rect属性，因为在主程序里要不断刷新显示此小鸟的运动后的位置。下面作用也是如此

    def move_left(self):
        self.speed=[-2,0]
        if self.rect.left<=0:
            self.rect.left=0
        else:
            self.rect=self.rect.move(self.speed)

    def move_up(self):
        self.speed=[0,-2]
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect=self.rect.move(self.speed)
        
    def move_down(self):
        self.speed=[0,2]
        if self.rect.bottom>=337:
            self.rect.bottom=337
        else:
            self.rect=self.rect.move(self.speed)