from inicio import Inicio
from fase import Fase
import pygame

class Gerenciador_Telas():
    def __init__(self, screen):
        self.screen = screen
        self.level = Inicio()
    
    def game_loop(self):
        game = True

        while game:
            game = self.screen_update()
            self.draw()

    def screen_update(self):
        next_level = self.level.update()
        if next_level == -1:
            return False
        if next_level == "GAME_SCREEN":
            self.level = Fase(1000, 500, "Astro Ape", "assets\\bg_space.png")
        return True

    def draw(self):
        self.level.draw()

        pygame.display.update()