import pygame
class Bird(): 
    def __init__(self,birdimg) -> None: #此份文件一定要配合L9.py以后的文件使用，新增了一个从L9.py主程序中传入的变量参数birdimg。实现了从主程序到类程序的数据传输
        position=100,130 
        self.img=pygame.image.load(birdimg) #调用从L9.py传入的参数值，实现动态改变小鸟的形态图片
        self.rect=self.img.get_rect(center=position)



    def move_right(self):
        self.speed=[2,0]
        if self.rect.right>=600:
            self.rect.right=600
        else:
            self.rect=self.rect.move(self.speed)

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