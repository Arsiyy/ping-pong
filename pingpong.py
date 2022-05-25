from pygame import *
init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (15, 150))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class PlayerOne(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
class PlayerTwo(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
class Ball(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (36, 36))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.y > win_height-36 or self.rect.y <= 0:
            self.speed_y = -self.speed_y

        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            self.speed_x = -self.speed_x

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
keys_pressed = key.get_pressed()
player1 = PlayerOne('pingpongrocket.png', 50, 250, 5)
player2 = PlayerTwo('pingpongrocket.png', 635, 250, 5)
ball = Ball('ball.png', 350-36, 250-36, 5, 5)
font.init()
font = font.Font(None, 70)
player1goal = 0
player2goal = 0
schet = font.render('счет: '+str(player1goal)+":"+str(player2goal), True, (255, 215, 0))

win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('пинг понг')
background = transform.scale(image.load("background.png"), (700, 500))
game = True
finish = False
while game:
    
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        player1.update()
        player2.update()
        ball.update()
        schet = font.render('счет: '+str(player1goal)+":"+str(player2goal), True, (255, 215, 0))
        if ball.rect.x < 0:
            player2goal += 1
            ball.rect.x = 350
            ball.rect.y = 250
            print('2 игрок забил гол')
        if ball.rect.x > win_width:
            player1goal
            player1goal +=1
            ball.rect.x = 350
            ball.rect.y = 250
            print('1 игрок забил гол')
        window.blit(schet, (350, 50))
        player1.reset()
        player2.reset()
        ball.reset()
        if player1goal == 11:
            end = font.render("победил игрок 2", True, (255, 215, 0))
        if player2goal == 11:
            end = font.render("победил игрок 1", True, (255, 215, 0))
        if player2goal == 11 or player1goal == 11:
            finish = True
            window.blit(end, (300, 250))
    if finish:
        window.blit(end, (300, 250))
    display.update()