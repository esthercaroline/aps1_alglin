import numpy as np
import pygame
from pygame.locals import *
import math
from monkey import Monkey

pygame.init()

class Fase():
    def __init__(self, width, height, title, bg_path):
        self.width = width
        self.height = height 
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.image.load(bg_path)
        self.background = pygame.transform.scale(self.background, (width, height))
        self.platform_rect = pygame.Rect(100, (self.height-80), 200, 40)
        self.target_rect = pygame.Rect(700, (self.height-300), 60, 60)
        self.monkey = Monkey(200, self.platform_rect.top - 70)
        pygame.display.set_caption(title)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 255), self.platform_rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.target_rect)
        self.monkey.draw()

    def update(self):     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.monkey.mouse_clicked = True

        if self.monkey.monkey_rect.colliderect(self.target_rect):
            self.monkey.reset()
        if self.monkey.monkey_rect.colliderect(self.platform_rect):
            self.monkey.on_platform = True
            
        self.monkey.update()