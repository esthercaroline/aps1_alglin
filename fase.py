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
        self.banana = pygame.Rect(400, (self.height-400), 20, 60)
        self.constant_banana = 3000
        self.monkey = Monkey(200, self.platform_rect.top - 70)
        pygame.display.set_caption(title)
        self.heart_image = pygame.image.load("assets\heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (20, 20))

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 255), self.platform_rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.target_rect)
        pygame.draw.rect(self.screen, (255, 255, 0), self.banana)
        self.monkey.draw()

        # Desenhe os corações indicando as vidas
        for i in range(self.monkey.lives):
            self.screen.blit(self.heart_image, (20 + i * 40, 20))

    def update(self):     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.monkey.mouse_clicked = True

        # Verficar se o macaco colidiu com a plataforma e com o alvo
        if self.monkey.monkey_rect.colliderect(self.target_rect):
            self.monkey.reset()
        if self.monkey.monkey_rect.colliderect(self.platform_rect):
            self.monkey.on_platform = True

        # Verifica a colisão do macaco com a banana e diminui as vidas
        if self.monkey.monkey_rect.colliderect(self.banana):
            self.monkey.reset()

        self.monkey.update(np.array([self.banana.x, self.banana.y]), self.constant_banana)