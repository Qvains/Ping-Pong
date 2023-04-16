# -- coding: cp1251 --
from pygame import *
from random import *
mixer.init()
font.init()
w = 720
h = 480
display.set_caption('Ping Pong')
window = display.set_mode((w,h))
back = (3, 166, 241)
class Board(sprite.Sprite):
    def __init__(self,Image,x,speed,w,h):
        super().__init__()
        self.Image = transform.scale(image.load(Image),(w,h))
        self.rect = self.Image.get_rect()
        self.w = w
        self.h = h
        self.rect.x = x
        self.rect.y = h / 2 + self.h
        self.speed = speed
        self.points = 0
    def update(self,Buttons : list):
        keys = key.get_pressed()
        if keys[Buttons[0]] and self.rect.y  >= 0:
            self.rect.y -= self.speed
        if keys[Buttons[1]] and self.rect.y + self.h <= h:
            self.rect.y += self.speed
    def reset(self):
        window.blit(self.Image,(self.rect.x,self.rect.y))
TEXT = font.SysFont(None,70) 
TEXT2 = font.SysFont(None,40) 
rocket_1  = Board('desk.png',100,5,25,120)
rocket_2  = Board('desk.png',w - 150,5,25,120)
Ball = transform.scale(image.load('ball.png'),(40,40))
Ball_rect = Ball.get_rect()
Ball_rect.x = w /2 + 25
Ball_rect.y = h /2 + 25
speed_x = 2
speed_y = 2
FPS = 60
res = 'None'
game = True
Clock = time.Clock()
while game:
    for e in event.get():
       if e.type == QUIT:
          game = False
    if res == 'None':
        if Ball_rect.colliderect(rocket_2.rect) or Ball_rect.colliderect(rocket_1.rect):
            speed_x = randint(2,4) if speed_x > 0 else -(randint(2,4))
            speed_x *= -1
        if Ball_rect.y + 40 >= h or Ball_rect.y <= 1:
            speed_y = randint(2,4) if speed_y > 0 else -(randint(2,4))
            speed_y *= -1
        Ball_rect.x += speed_x
        Ball_rect.y += speed_y
        if Ball_rect.x + 1<= 120:
            rocket_2.points += 1
            Ball_rect.x = w /2 + 25
            Ball_rect.y = h /2 + 25
            speed_x *= -1
            speed_y *= -1
        elif Ball_rect.x - 1 >= w - 175:
            rocket_1.points += 1
            Ball_rect.x = w /2 + 25
            Ball_rect.y = h /2 + 25
            speed_x *= -1
            speed_y *= -1
        window.fill(back)
        window.blit(TEXT.render(str(rocket_1.points)+ '/5',True,(0,0,0)),(20,10))
        window.blit(TEXT.render(str(rocket_2.points)+ '/5',True,(0,0,0)),(w - 80,10))
        window.blit(Ball,(Ball_rect.x,Ball_rect.y))
        rocket_1.update([K_w,K_s])
        rocket_2.update([K_UP,K_DOWN])
        rocket_1.reset()
        rocket_2.reset()
        res = 'Левый' if rocket_1.points >= 5 else 'Правый' if rocket_2.points >= 5 else 'None'
    else:
        window.blit(TEXT2.render(f'Выиграл {res} игрок',True,(0,0,0)),(20,100))
        window.blit(TEXT2.render('Нажмите ЛКМ чтобы начать заново',True,(0,0,0)),(20,250))
        mice = mouse.get_pressed()
        if mice[0]:
            res = 'None'
            rocket_1.points = 0
            rocket_2.points = 0
        
    display.update()
    Clock.tick(FPS)