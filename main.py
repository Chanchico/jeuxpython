import pygame as pg
from game import Game
import time

pg.init()

pg.display.set_caption("Comet fall game")
screen = pg.display.set_mode((1080, 720))

#chargement arrière plan
background = pg.image.load('assets/bg.jpg')

#chargement joueur
game = Game()

running = True

while running:

    #application de l'arrière plan
    screen.blit(background, (0, -200))

    #application dduu joueur
    screen.blit(game.player.image, game.player.rect)

    #recuperer les projectiles pour les faire bouger
    for projectile in game.player.all_projectiles:
        projectile.move()

    #recuperer les monstres du jeu pour les faire bouger
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # application de l'ensembles des images de mon groupe de pojectiles
    game.player.all_projectiles.draw(screen)

    #appliquer l'ensemble des images du groupe monstre
    game.all_monsters.draw(screen)

    #verifier si le joueur souhait aller à gauche ou à droite
    if game.pressed.get(pg.K_RIGHT) and  game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pg.K_LEFT) and  game.player.rect.x > 0:
        game.player.move_left()

    # mise a jour de l'écran
    pg.display.flip()

    for event in pg.event.get() :
        if event.type == pg.QUIT:
            running = False
            pg.quit()

        #detecter si un joueur lache une touche du clavier
        elif event.type == pg.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pg.K_SPACE:
                game.player.lauch_projectile()

        elif event.type == pg.KEYUP:
            game.pressed[event.key] = False
