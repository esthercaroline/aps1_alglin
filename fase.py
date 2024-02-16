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
        monkey_y = platform_rect.top - 100 
        monkey_x = platform_rect.left + 140
        self.monkey.initial_y = monkey_y
        self.monkey.initial_x = monkey_x
        self.monkey.draw()
        
    # esses métodos serão usados nas classes de cada objeto (no update)
    # def gravity(g, distance):
    #     return g / (distance**0.5)
    
    # def distance(x1, y1, x2, y2):
    #     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5