import pygame
from gerenciador_telas import Gerenciador_Telas

pygame.init()
pygame.display.set_caption("Astro Ape")
screen = pygame.display.set_mode((1000, 500))
level = Gerenciador_Telas(screen)
level.game_loop() 