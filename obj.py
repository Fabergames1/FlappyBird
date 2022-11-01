import pygame


class Obj(pygame.sprite.Sprite):

    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y


class Pipe(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

    def update(self, *args):
        self.move()

    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()


class Coin(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)



        self.ticks = 0

    def update(self, *args):
        self.move()
        self.anim()

    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()

    def anim(self):
        self.ticks = (self.ticks + 1) % 6
        self.image = pygame.image.load("assets/" + str(self.ticks) + ".png")


class Bird(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound("assets/sounds/point.ogg")
        self.sound_hit = pygame.mixer.Sound("assets/sounds/hit.ogg")
        self.sound_fly = pygame.mixer.Sound("assets/sounds/wing.ogg")

        self.ticks = 0
        self.vel = 4
        self.grav = 1

        self.pts = 0

        self.play = True

    def update(self, *args):
        self.anim()
        self.move()

    def anim(self):
        self.ticks = (self.ticks + 1) % 4
        self.image = pygame.image.load("assets/bird" + str(self.ticks) + ".png")

    def move(self):

        self.vel += self.grav
        self.rect[1] += self.vel

        if self.vel >= 15:
            self.vel = 15

        if self.rect[1] >= 440:
            self.rect[1] = 440
        elif self.rect[1] <= 0:
            self.rect[1] = 0
            self.vel = 4

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.vel -= 10
                self.sound_fly.play()

    def colision_pipes(self, group):

        col = pygame.sprite.spritecollide(self, group, False)

        if col:
            self.play = False
            self.sound_hit.play()

    def colision_coin(self, group):

        col = pygame.sprite.spritecollide(self, group, True)

        if col:
            self.pts += 1
            self.sound_pts.play()


class Text:

    def __init__(self, size, text):

        self.font = pygame.font.Font("assets/font/font.ttf", size)
        self.render = self.font.render(text, True, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def text_update(self, text):
        self.render = self.font.render(text, True, (255, 255, 255))
