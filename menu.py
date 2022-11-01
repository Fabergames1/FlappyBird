from obj import Obj, Text
import pygame


class Menu:

    def __init__(self):

        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)

        self.get_ready = Obj("assets/getready.png", 60, 100, self.all_sprites)
        self.table_score = Obj("assets/score.png", 20, 200, self.all_sprites)
        self.button_go = Obj("assets/go.png", 100, 420, self.all_sprites)

        self.change_scene = False

        self.text_score = Text(100, "0")

    def draw(self, window):
        self.all_sprites.draw(window)
        self.text_score.draw(window,160, 250)

    def update(self, pts):
        self.all_sprites.update()
        self.move_bg()
        self.move_ground()
        self.text_score.text_update(pts)

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_go.rect.collidepoint(pygame.mouse.get_pos()):
                self.change_scene = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.change_scene = True

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