# Game

import pygame as pg
import random
from constants import *
from sprites import *


class game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width,height))
        #self.background = pg.image.load("level_1.png")
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = True


    def new(self):
        # Start new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Mario(self)
        self.all_sprites.add(self.player)
        self.p1 = Platform(0, 536, 2953, 60)
        self.platforms.add(self.p1)
        self.all_sprites.add(self.p1)
        for plat in platform_list:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()


    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # Game loop update
        self.all_sprites.update()
        # game over condition
        if self.player.rect.y > height:
            self.playing = False
        # check if player hits the platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
        # for screen scrollig in right direction
        '''if self.player.rect.top <= height/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)'''


    def events(self):
        # Game loop events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False


    def draw(self):
        # Game loop - draw
        self.screen.fill(black)
        self.all_sprites.draw(self.screen)
        # After drawing everything flip the display
        pg.display.flip()


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
quit()
