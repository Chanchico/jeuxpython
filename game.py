import pygame as pg
from player import Player
from monster import Monster


class Game:
    def __init__(self):
        # genener notre joueur
        self.all_players = pg.sprite.Group()
        self.player = Player(self)
        self.all_players .add(self.player)
        # groupe de monstre
        self.all_monsters = pg.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)
