from obj import Obj, Pipe, Coin, Bird, Text
import pygame
import random


class Game:

    def __init__(self):

        self.all_sprites = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.pipes_group = pygame.sprite.Group()

        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)

        self.score = Text(100, "0")

        self.bird = Bird("assets/bird1.png", 50, 320, self.all_sprites)

        self.change_scene = False

        self.ticks = 0
        self.timer = 0

        self.max_score = 0
        self.check_score()

    def draw(self, window):
        self.all_sprites.draw(window)
        self.score.draw(window, 160, 50)

    def update(self):
        self.move_bg()
        self.move_ground()

        if self.bird.play:
            self.spaw_pipes()
            self.bird.colision_coin(self.coin_group)
            self.bird.colision_pipes(self.pipes_group)
            self.score.text_update(str(self.bird.pts))
            self.all_sprites.update()
        else:
            self.save_score()
            self.gameover()

    def move_bg(self):
        self.bg.rect[0] -= 1
        self.bg2.rect[0] -= 1

        if self.bg.rect[0] <= -360:
            self.bg.rect[0] = 0
        if self.bg2.rect[0] <= 0:
            self.bg2.rect[0] = 360

    def move_ground(self):
        self.ground.rect[0] -= 3
        self.ground2.rect[0] -= 3

        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0
        if self.ground2.rect[0] <= 0:
            self.ground2.rect[0] = 360

    def spaw_pipes(self):
        self.ticks += 1

        if self.ticks >= random.randrange(80, 110):
            self.ticks = 0
            pipe = Pipe("assets/pipe1.png", 360, random.randrange(300, 450), self.all_sprites, self.pipes_group)
            pipe2 = Pipe("assets/pipe2.png", 360, pipe.rect[1] - 550, self.all_sprites, self.pipes_group)
            coin = Coin("assets/0.png", 388, pipe.rect[1] - 120, self.all_sprites, self.coin_group)

    def gameover(self):
        self.timer += 1
        if self.timer >= 30:
            self.change_scene = True

    def save_score(self):
        if self.bird.pts > self.max_score:
            self.max_score = self.bird.pts
            file = open("save.txt", "w")
            file.write(str(self.max_score))
            file.close()

    def check_score(self):
        file = open("save.txt", "r")
        self.max_score = int(file.read())
        file.close()

