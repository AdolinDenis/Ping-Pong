from pygame import *

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
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('Ping Pong')

background = transform.scale(image.load('background.jpg'), (700, 500))

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 10, 100, 5)
racket2 = Player('racket.png', 660, 200, 10, 100, 5)
ball = GameSprite('pingpongball.png', 200, 200, 50, 50, 3)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('Player 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0, 0))
        racket1.update1()
        racket2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True

        if ball.rect.x > 675:
            finish = True
            window.blit(lose2, (200, 200))
            game = True

        racket1.reset()
        racket2.reset()
        ball.reset()

    clock.tick(FPS)
    display.update()
