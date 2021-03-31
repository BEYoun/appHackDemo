import pygame
from comet import Comet


class CometFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 33
        self.game = game

        # definir un groupe de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loading(self):
        return self.percent >= 100


    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # se declence quand la jauge dev eet charger
        if self.is_full_loading():
            print('pluie de cometes !!')
            self.meteor_fall()
            self.reset_percent()

    def update_bar(self, surface):
        # ajout du pourcentage a la bare
        self.add_percent()
        # appel de mete poyur declencher comet
        self.attempt_fall()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 20,
            surface.get_width(), # longeur
            10 #epaiseur
        ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,
            (surface.get_width()/100)*self.percent,  # longeur
            10  # epaiseur
        ])