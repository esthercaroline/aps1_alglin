import pygame
from pygame.locals import *
import math
import numpy as np


class Monkey:
    def __init__(self, x, y, width=1000, height=500, lives=5): # Adicione o atributo lives
        self.initial_pos = np.array([x, y])
        self.initial_speed = np.array([10, -10])
        self.gravity = np.array([0, 0.03])
        self.screen = pygame.display.set_mode((width, height))
        self.image = pygame.transform.scale(pygame.image.load("assets\macaco.png"), (100, 100))
        self.monkey_rect = self.image.get_rect()
        self.speed = self.initial_speed
        self.position = self.initial_pos
        self.mouse_clicked = False
        self.on_platform = True
        self.lives = lives  # Inicialize o atributo lives

    def update(self, banana_pos, constant):
        if self.mouse_clicked and self.on_platform:
            mouse_pos = np.array(pygame.mouse.get_pos())
            direction = mouse_pos - self.position
            if np.linalg.norm(direction) != 0:
                direction = direction.astype(float) / np.linalg.norm(direction)
            self.speed = direction * 5
            self.mouse_clicked = False
            self.on_platform = False

            if (self.position[1] < 0 or self.position[1] > 400) or (self.position[0] < 0 or self.position[0] > 900):
                self.initial_speed = pygame.mouse.get_pos() - self.initial_pos
                self.initial_speed = (self.initial_speed / np.linalg.norm(self.initial_speed)) * 5
                self.speed = self.initial_speed
                self.position = self.initial_pos

        if not self.on_platform:
            # Calculating attraction towards banana
            direction_to_banana = banana_pos - self.position
            distance_to_banana = np.linalg.norm(direction_to_banana)
            if distance_to_banana != 0:
                attraction_force = (constant / distance_to_banana**2) * (direction_to_banana / distance_to_banana)
                self.speed += attraction_force

            self.speed += self.gravity
            self.monkey_rect.topleft = self.position
            self.position = self.position + self.speed

            if self.position[1] > 500 or self.position[0] > 1000 or self.position[0] < 0 or self.position[1] < 0:
                self.reset()

    def reset(self):
        if self.lives > 0:  # Verifique se há vidas restantes
            self.lives -= 1 
            self.position = self.initial_pos
            self.speed = self.initial_speed
            self.mouse_clicked = False
            self.on_platform = True
        else:
            # ANA COLOCA PRA TELA DE GAMEOVER
            pass

    def draw(self):
        self.monkey_rect.topleft = self.position
        self.screen.blit(self.image, self.monkey_rect)
