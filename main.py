import pygame
from manage_screens import ManageScreen

pygame.init()
pygame.display.set_caption("Astro Ape")
screen = pygame.display.set_mode((1000, 500))
level = ManageScreen(screen)
level.game_loop() 