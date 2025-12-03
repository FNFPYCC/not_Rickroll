from pygame import *

window = display.set_mode((700,500))
display.set_caption('Догонялки')
background = transform.scale(image.load("background.jpg"), (700,500))
window.blit(background,(0,0))

mixer.init()

clock = time.Clock()
fps = 60

jungles = mixer.Sound("jungles.ogg")
money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")
rick = mixer.Sound('rick-astley-never-gonna-give-you-up_9j9vMfn.mp3')
win_width = 700
win_height = 500

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,r_x,r_y):
        super().__init__()
        self.r_x = r_x
        self.r_y = r_y
        self.image = transform.scale(image.load(player_image),(r_x,r_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed,r_x,r_y):
        super().__init__(player_image,player_x,player_y,player_speed,r_x,r_y)
        self.direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x > win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

#class Font()

wall = Wall(250, 128, 114,300,0,10,360)
wall1 = Wall(250, 128, 114,180,100,10,260)
wall2 = Wall(250, 128, 114,180,360,130,10)
wall3 = Wall(250, 128, 114,100,100,80,10)
wall4 = Wall(250, 128, 114,0,200,80,10)
wall5 = Wall(250, 128, 114,100,300,80,10)
wall6 = Wall(250, 128, 114,460,100,10,400)

#hero = transform.scale(image.load('hero.png'),(50,50))
cyborg = Enemy('cyborg.png',650,300,2,65,65)

player = Player('hero.png',200,290,2.5,65,65)
test = Player('treasure.png',560,400,0,65,65)
game_over_0 = Player('689368f40e271.png',160,200,0,380,57)
you_win = Player('68936d5ac26f5.png',200,200,0,277,57)
rickroll = Player('rickroll-roll.gif',0,0,0,700,500)


finish = False

x1 = 0
y1 = 450

cyborg_x = 650
cyborg_y = 300
cyborg_s = True

notwin = False
game_over = False

b = 0
b1 = 0

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    #jungles.play()
    
    
    
    test.reset()
    test.update()
    cyborg.reset()
    cyborg.update()
    wall.draw_wall()
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()

    
    #window.blit(hero,(x1,y1))
    

    if game_over == False:
        if sprite.collide_rect(player,cyborg):
            game_over = True
            kick.play()
        if sprite.collide_rect(player,wall):
            game_over = True
        if sprite.collide_rect(player,wall1):
            game_over = True
        if sprite.collide_rect(player,wall2):
            game_over = True
        if sprite.collide_rect(player,wall3):
            game_over = True
        if sprite.collide_rect(player,wall4):
            game_over = True
        if sprite.collide_rect(player,wall5):
            game_over = True
        if sprite.collide_rect(player,wall6):
            game_over = True
        
    if game_over == True:
        rickroll.reset()
        rickroll.update()
        if b1 == 0:
            rickroll.reset()
            rickroll.update()
            b1 = 1
            rick.play()
        game_over_0.reset()
        game_over_0.update()
        notwin = True

    if notwin == False:
        player.reset()
        player.update()

    if finish == False:
        if sprite.collide_rect(player,test):
            finish = True
            b += 2
            if b == 2:
                money.play()
                b += 1
            notwin = True
    if finish == True:
        you_win.reset()
        you_win.update()
    display.update()
    clock.tick(fps)

#создай окно игры

#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»
