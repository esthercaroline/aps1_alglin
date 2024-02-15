import numpy as np
import pygame
from pygame.locals import *
import math

pygame.init()

class Fase:
    def __init__(self, largura, altura, titulo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.rodando = True
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(titulo)

    def desenhar(self):
        self.tela.fill((0, 0, 0))
        pygame.display.flip()

    def executar(self):
        while self.rodando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False

            self.desenhar()

        pygame.quit()