# sprite classes for platform game
from constants import *
import pygame as pg

vec = pg.math.Vector2


class SpriteSheet:
    #utility class for loading and parsing SpriteSheet
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert_alpha()

    def get_image(self, x, y, w, h):
        # grab an image out of larger SpriteSheet
        image = pg.Surface((w, h))
        image.blit(self.spritesheet, (0, 0), (x, y, w, h))
        image = pg.transform.scale(image,(w*3, h*3))
        return image


class Mario(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30,40))
        self.image.fill(green)
        #spritesheet = SpriteSheet("player.png")
        #self.image = spritesheet.get_image(178, 32, 16, 16)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2 , height/2)
        self.pos = vec(width/2 , height/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            if self.pos.x >= width/4:
                self.acc.x = -player_acc
            else:
                if self.game.p1.rect.x < 0:
                    for plat in self.game.platforms:
                        plat.rect.x += 5
                elif self.rect.x > 0:
                    self.acc.x = -player_acc
        if keys[pg.K_RIGHT]:
            if self.pos.x <= width*3/4:
                self.acc.x = player_acc
            else:
                if self.game.p1.rect.x >= -8140:
                    for plat in self.game.platforms:
                        plat.rect.x -= 5
                elif self.rect.right < width:
                    self.acc.x = player_acc


        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            if keys[pg.K_SPACE]:
                self.vel.y = -15

        self.acc.x += self.vel.x * player_friction
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        self.rect.midbottom = self.pos



class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
