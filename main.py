
import pygame
from pygame.locals import *
import math
from fase import Fase
from monkey import Monkey

fase = Fase(1000, 500, "Astro Ape", "assets\\bg_space.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            fase.monkey.mouse_clicked = True

    fase.update()

    fase.screen.fill((255, 255, 255))
    
    fase.draw()

    pygame.display.flip()

pygame.quit()