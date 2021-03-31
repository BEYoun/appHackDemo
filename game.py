from player import Player
from monster import  Monster
from comet_event import CometFallEvent
import pygame


# class jeux
class Game:
    def __init__(self):
        # condition du jeux
        self.is_playing = False
        # generer notre joueur
        self.all_players =  pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer event comet
        self.comet_event = CometFallEvent(self)
        #groupe de monter
        self.all_mosnter = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing=True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        self.all_mosnter = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        self.player.update_health_bar(screen)

        # actualiser bare de jeux
        self.comet_event.update_bar(screen)


        # actualister animation joueur
        self.player.update_animation()

        # recuperer les projectil dans le joueur
        for projectile in self.player.all_projectile:
            projectile.move()

        for monster in self.all_mosnter:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recupeter les comet
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer le joueur dans notre ecran
        screen.blit(self.player.image, self.player.rect)

        # applique le greoupe de projectile
        self.player.all_projectile.draw(screen)

        # les monster apparition
        self.all_mosnter.draw(screen)

        # apparition des comet
        self.comet_event.all_comets.draw(screen)

        # verifier mouvement joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_mosnter.add(monster)

