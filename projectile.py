import pygame as pg


class Projectile(pg.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pg.image.load('assets/projectile.png')
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner projectile
        self.angle += 12
        self.image = pg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rotate()
        self.rect.x += self.velocity
        #verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()

            monster.damage(self.player.attack)
            print('toucher')

         #destruction de projectile quand il sort de la fenetre
        if self.rect.x > 1080:
            print('p destroy')
            self.remove()

