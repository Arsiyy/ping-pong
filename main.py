import pygame as pg
pg.init()
win_width = 700
run = True
win_height = 500
finish = False
class GameSprite(pg.sprite.Sprite):
    def __init__(self, picture, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (width, height))
        self.speed = speed
        self.height = height
        self.width = width
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
main_win = pg.display.set_mode((win_width, win_height))
pg.display.set_caption('пинг понг')
bg = pg.image.load('fon.jpg')
bg = pg.transform.scale(bg, (win_width, win_height))
#bg = pg.transform.scale(pg.image.load("fon.jpg"), (win_width, win_height))
while run:
    if not finish:
        keys = pg.key.get_pressed()
        for e in pg.event.get():
            if e.type == pg.QUIT or keys[pg.K_ESCAPE]:
               run = False
       # main_win.blit(bg, (0, 0))
    pg.display.update()
    pg.time.delay(5)
# #Создай собственный Шутер!
# from pygame import *
# font.init()

# win_width = 700
# win_height = 500
# main_win = display.set_mode((win_width, win_height))
# display.set_caption('пинг понг')
# lost = 0
# score = 0
# max_lost = 3
# max_score = 10

# class GameSprite(sprite.Sprite):
#     def __init__(self, picture, x, y, width, height, speed):
#         super().__init__()
#         self.image = transform.scale(image.load(picture), (width, height))
#         self.speed = speed
#         self.height = height
#         self.width = width
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y

#     def reset(self):
#         main_win.blit(self.image, (self.rect.x, self.rect.y))

# # class Player(GameSprite):
# #     def update(self):
# #         keys_pressed = key.get_pressed()
# #         mouse_x, mouse_y = pyautogui.position()
# #         if mouse_x > 0 and mouse_x < win_width-50:
# #             self.rect.x = mouse_x
# bg = transform.scale(image.load("fon.jpg"), (win_width, win_height))
# player = Player("playerpng1.png", win_width/2-25, win_height-105, 50, 100, 10)
# font_UI = font.SysFont('Arial', 36)
# run = True
# finish = False
# while run:
# #    for e in event.get():
# #        if e.type == QUIT or keys[K_ESCAPE]:
# #            run = False
#     main_win.blit(bg, (0, 0))
# ##    player.update()
#     # player.reset()
#     display.update()
#     time.delay(5)
