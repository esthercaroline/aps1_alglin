import numpy as np
import pygame
from pygame.locals import *
import math

pygame.init()

class Fase:
    def __init__(self, width, height, title, bg_path):
        self.width = width
        self.height = height 
        self.title = title
        self.running = True
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.image.load(bg_path)
        self.background = pygame.transform.scale(self.background, (width, height))
        pygame.display.set_caption(title)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 255), (self.width-700, (self.height-70), 400, 50))
        pygame.display.flip()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

        pygame.quit()

    # esses métodos serão usados nas classes de cada objeto (no update)
    # def gravity(g, distance):
    #     return g / (distance**0.5)
    
    # def distance(x1, y1, x2, y2):
    #     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5