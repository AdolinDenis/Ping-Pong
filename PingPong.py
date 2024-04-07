from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Ping Pong')

background = transform.scale(image.load('background.jpg'), (700, 500))

clock = time.Clock()
FPS = 60
speed_x = 5
speed_y = 5

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 25:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < 475:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
            self.rect.x += speed_x
            self.rect.y += speed_y
        


game = True
while game:
    window.blit(background, (0, 0))
    #window.blit(sprite1, (x1, y1))
    #window.blit(sprite2, (x2, y2))
    clock.tick(FPS)
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
