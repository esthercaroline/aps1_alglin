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
        self.target_rect = pygame.Rect(700, (self.height-300), 100, 100)
        self.target_planet = pygame.image.load("assets\planet_orange.png")
        self.target_planet = pygame.transform.scale(self.target_planet, (100, 100))
        self.banana_rect = pygame.Rect(400, (self.height-400), 60, 80)
        self.banana = pygame.image.load("assets\solo_banana_png.png")
        self.banana = pygame.transform.scale(self.banana, (60, 80))
        self.constant_banana = 3000
        self.monkey = Monkey(200, self.platform_rect.top - 70)
        pygame.display.set_caption(title)
        self.heart_image = pygame.image.load("assets\heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (20, 20))

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 255), self.platform_rect)
        self.screen.blit(self.target_planet, (self.target_rect.x, self.target_rect.y))
        self.screen.blit(self.banana, (self.banana_rect.x, self.banana_rect.y))
        self.monkey.draw()

        # Desenha os corações indicando as vidas
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
            return "NEXT_LEVEL"
        if self.monkey.position[0] == self.monkey.initial_pos[0] and self.monkey.position[1] == self.monkey.initial_pos[1]:	
            self.monkey.on_platform = True

        # Verifica a colisão do macaco com a banana e diminui as vidas
        if self.monkey.monkey_rect.colliderect(self.banana_rect):
            if self.monkey.lives > 1:
                self.monkey.reset()
            elif self.monkey.lives == 1:
                return "GAME_OVER"

        self.monkey.update(np.array([self.banana_rect.x, self.banana_rect.y]), self.constant_banana)