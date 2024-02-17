import pygame
from pygame.locals import *
import math
import numpy as np

# Inicia a classe Monkey
class Monkey:
    def __init__(self, x, y, width = 1000, height = 500):
        self.initial_pos = np.array([x, y])
        self.initial_speed = np.array([10, -10])
        self.gravity = np.array([0, 0.1])
        self.screen = pygame.display.set_mode((width, height))
        self.image = pygame.transform.scale(pygame.image.load("assets\macaco.png"), (100, 100))
        self.speed = self.initial_speed
        self.position = self.initial_pos

    def update(self):
        if (self.position[1] < 0 or self.position[1] > 400) or (self.position[0] < 0 or self.position[0] > 900):
            self.initial_speed = pygame.mouse.get_pos() - self.initial_pos
            self.initial_speed = (self.initial_speed / np.linalg.norm(self.initial_speed)) * 5
            self.speed = self.initial_speed
            self.position = self.initial_pos
        
        self.position = self.position + self.speed

    def draw(self):
        self.screen.blit(self.image, self.position)