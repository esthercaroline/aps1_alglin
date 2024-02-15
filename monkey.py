import pygame
from pygame.locals import *
import math

# Inicia a classe Monkey
class Monkey:
    def __init__(self, x, y):
        self.initial_x = x
        self.initial_y = y
        self.image = pygame.image.load("monkey_sem_capacete.webp")
        self.initial_speed = 0
        self.speed = 0
        self.monkey_mass = 1

    def update(self):
        self.initial_x += self.speed
        self.initial_y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.initial_x, self.initial_y))

    # def jump(self):
    #     self.speed = -10

    # def fall(self):
    #     self.speed = 10

    # def stop(self):
    #     self.speed = 0

    # def move_left(self):
    #     self.speed = -10

    # def move_right(self):
    #     self.speed = 10

    # def stop_x(self):
    #     self.speed = 0

    # def move_up(self):
    #     self.y -= 10

    # def move_down(self):
    #     self.y += 10

    # def stop_y(self):
    #     self.y = 0

    # def get_position(self):
    #     return (self.x, self.y)

    # def set_position(self, x, y):
    #     self.x = x
    #     self.y = y