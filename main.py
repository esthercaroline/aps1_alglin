
import pygame
from pygame.locals import *
import math
from fase import Fase
from monkey import Monkey

fase = Fase(1000, 500, "Astro Ape", "assets\\bg_space.png")
monkey = Monkey(400, 300)
fase.execute()
