import numpy as np
import pygame
from pygame.locals import *
import math

pygame.init()

class Fase:
    def __init__(self, width, height , title):
        self.width = width
        self.height = height 
        self.title = title
        self.running = True
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

        pygame.quit()

    def gravity(self, x, y, g, t):
        return x, y + (1/2) * g * t ** 2