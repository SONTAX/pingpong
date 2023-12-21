from pygame import *
from random import randint


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
            self.rect.y += self.speed
        if keys[K_s] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y -= self.speed

    def update_second(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 0:
            self.rect.y += self.speed
        if keys[K_l] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y -= self.speed


WIDTH = 800
HEIGHT = 600
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping Pong")

player1 = Player("sprite1.png", 30, 300, 30, 100, 6)
player2 = Player("sprite2.png", 740, 300, 30, 100, 6)

game = True
run = True
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255,255,255))
    if run:
        player1.update_first()
        player2.update_second()
        player1.reset()
        player2.reset()
    display.update()
    clock.tick(60)
