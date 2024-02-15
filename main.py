import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame.locals import *
import math

# Inicializa o Pygame
pygame.init()

class Fase:
    def __init__(self, largura, altura, titulo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(titulo)

    def desenhar(self):
        self.tela.fill((0, 0, 0))
        pygame.display.flip()

fase = Fase(800, 600, "Astro Ape")

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    fase.desenhar()

pygame.quit()