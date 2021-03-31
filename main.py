import pygame
from game import Game
import math

pygame.init()




# generer la fenetre de notre jeux

pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# import background de notre jeux
background = pygame.image.load('./assets/bg.jpg')

# banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)


# Button
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)
# charger notre jeu
game = Game()


running = True

# boucle tant que running est vrai
while running:
    # aapliquer l'arrier plan de notre jeu
    screen.blit(background, (0, -200))
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()


    # si le joueur ferme la fenettre
    for event in pygame.event.get():
        # event de fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeux")
        # detect touch keyboard
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()