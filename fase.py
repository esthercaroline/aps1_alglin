import numpy as np
import pygame
from pygame.locals import *
import math
from monkey import Monkey

pygame.init()

class Fase:
    def __init__(self, width, height, title, bg_path):
        self.width = width
        self.height = height 
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.image.load(bg_path)
        self.background = pygame.transform.scale(self.background, (width, height))
        self.monkey = Monkey(200, 200)
        pygame.display.set_caption(title)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        platform_rect = pygame.Rect((self.width//2 -200), (self.height-70), 400, 50)
        pygame.draw.rect(self.screen, (0, 0, 255), platform_rect)
        self.monkey.draw()

    def update(self):
        self.monkey.update()