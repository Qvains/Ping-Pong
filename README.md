# Ping-Pong
from pygame import *
from random import *
mixer.init()
font.init()
w = 720
h = 480
FPS = 60
res = 'None'
game = True
Clock = time.Clock()
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
rocket_1  = Board('Desk.png',100,5,25,120)
rocket_2  = Board('Desk.png',w - 150,5,25,120)
Ball = transform.scale(image.load('Ball.png'),(40,40))
Ball_rect = Ball.get_rect()
Ball_rect.x = w /2 + 25
Ball_rect.y = h /2 + 25
speed_x = 2
speed_y = 2
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
    
    
    
    
#WARNING!!!!
#Возможен Баг с текстом



Это игра ping pong, или настольный теннис. 
Я использовал Библиотеки pygame и random. Вначале инициализировал pygame (font и mixer), задал переменные для игры (w,h,FPS,Clock и тд).
Создаю игровое окно, задаю название окна и цвет заднего фона (RGB).
Создаю класс Board для двух игроков, в нем описываются свойства (image,w,h,x,y,rect,speed,points). В Методе update описываю движение Board, учитывая то что она может уйти за пределы игрового окна. По переданному параметру в виде списка list в котором храняться кнопки, на которые нажимая будет перемещаться доска ( 1 элемент списка перемещение вверх, 2 вниз). Собираю Нажатые клавиши во время одной итерации цикла и ищу в списке кнопки, которые должны перемещать доску. В Методе reset рисую (обновляю) картинку  доски по собственным координатам. Создаю Тексты, Спрайты(Доски) и спрайт шарик, задавая его свойства только через переменный( не через класс).
Игровой Цикл
Обрабатываю выход из игры( если нажат крестик, то игра завершается)
Через переменную res, которая хранит в себе значени кто выиграл или None(неопределенно). Если None, игра продолжается. Обрабатываю столкновение Шарика с досками, стенками и уходом за доску. При столкновении с досками или стенками(горизонтальными) шарик меняет направление (с досками по x, со стенками по y). Также задаю рандомную скорость (2 или 3). Шарик пермещается. Далее проверяю если шарик ушел за доску,если да то противоположному игроку засчитывает очко, шарик появляется по середине поля и меняет направление по x и y. Окрашиваю фон, Рисую счетчик для каждого игрока, рисую шар, Делаю обработку положения досок(update) и рисую доски (обновляю).
делаю проверку если у кого счетчик 5 или больше. Также проверяю у кого счетчик больше, если у правого, то res ='Правый', иначе если у левого, то red = 'Левый'.
После если кто то выиграл, игра останавливаеться, так как переменная res уже не None, На экран выводится кто выиграл, и предлагается начать игру заново, если нажать
ЛКМ (mouse 1). Если нажата ЛКМ, то счетчики обновляются ( до 0), res = 'None'.
В конце цикла обновляю игровое окно и устанавливаю FPS.
Завершение Цикла.
