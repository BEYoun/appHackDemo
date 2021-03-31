import pygame
from projectile import Projectile
from animation import AnimateSprite

# class joueur
class Player(AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.veloity = 5
        self.all_projectile = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update_animation(self):
        self.animate()

    def damage(self, value):
        if self.health - value >0:
            self.health -= value
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):
        self.all_projectile.add(Projectile(self))
        #danimation
        self.start_animation()

    def move_right(self):
        if not self.game.check_colision(self, self.game.all_mosnter):
             self.rect.x += self.veloity

    def move_left(self):
        self.rect.x -= self.veloity
