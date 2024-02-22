import pygame
from manage_screens import ManageScreen

pygame.init()
pygame.display.set_caption("Astro Ape")
screen = pygame.display.set_mode((1000, 500))
musica = pygame.mixer.music.load('assets\space.mp3')
pygame.mixer.music.play(loops = -1)
pygame.mixer.music.set_volume(0.1)
level = ManageScreen(screen)
level.game_loop() 