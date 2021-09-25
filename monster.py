import pygame as pg
import time

class Monster(pg.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pg.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 1


    def damage(self, amount):
        # Infliger les degat
        self.health -= amount

        #tuer le monstre
        if self.health <= 0:
            #reapparitre comme nouveau monstres
            self.rect.x = 1000
            self.health = self.max_health



    def update_health_bar(self, surface):
        #definir couleur de la jauge de la vie
        barre_color = (111, 210, 46)
        barre_arriere = (60, 63, 60)

        #definir la position de la jauge de vie
        barre_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        barre_position_arriere = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        #dessiner barre de vie
        pg.draw.rect(surface, barre_arriere, barre_position_arriere)
        pg.draw.rect(surface, barre_color, barre_position)


    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):

            self.rect.x -= self.velocity
