import random

from pygame import *
from random import choice

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_first(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed

    def update_second(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        global score_1, score_2
        if self.rect.y < 0 or self.rect.y > HEIGHT - self.rect.height:
            self.y_speed *= -1
        if sprite.collide_rect(player1, self) or sprite.collide_rect(self, player2):
            self.x_speed *= -1
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x > WIDTH - self.rect.width:
            score_1 += 1
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2
            self.x_speed, self.y_speed = random.choice(speeds)
            self.x_speed *= random.choice([-1, 1])
            self.y_speed *= random.choice([-1, 1])
        if self.rect.x < 0:
            score_2 += 1
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2
            self.x_speed, self.y_speed = random.choice(speeds)
            self.x_speed *= random.choice([-1, 1])
            self.y_speed *= random.choice([-1, 1])


WIDTH = 1200
HEIGHT = 600
speeds = [(5, 5), (5, 10), (10, 5)]

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping Pong")

player1 = Player("sprite1.png", 30, (HEIGHT - 180) / 2, 30, 180, 6)
score_1 = 0
player2 = Player("sprite2.png", WIDTH - 60, (HEIGHT - 180) / 2, 30, 180, 6)
score_2 = 0

ball = Ball("ball.png", (WIDTH - 30) / 2, (HEIGHT - 30) / 2, 30, 30, 5)
ball.x_speed, ball.y_speed = random.choice(speeds)
ball.x_speed *= random.choice([-1, 1])
ball.y_speed *= random.choice([-1, 1])


font.init()
FONT = font.SysFont("comic sans ms", 30, True)

game = True
run = True
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((100, 100, 100))
    if run:
        draw.aaline(window, (0, 0, 0), (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
        player1.update_first()
        player2.update_second()
        ball.update()
        score = FONT.render(str(score_1) + "     " + str(score_2), True, (0, 0, 0))
        window.blit(score, ((WIDTH - 100) / 2, 100))
        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(60)
