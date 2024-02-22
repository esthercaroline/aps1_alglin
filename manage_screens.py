from start import Start
from fase import Fase
from instructions import Instructions
from game_over import GameOver
from Victory import Victory
import pygame

class ManageScreen():
    def __init__(self, screen):
        self.screen = screen
        self.level = Start()
    
    def game_loop(self):
        game = True

        while game:
            game = self.screen_update()
            self.draw()

    def screen_update(self):
        next_level = self.level.update()
        if next_level == -1:
            return False
        elif next_level == "GAME_SCREEN":
            self.level = Fase(1000, 500, "Astro Ape", "assets\\bg_space.png")
        elif next_level == "INSTRUCTIONS_SCREEN":
            self.level = Instructions()
        elif next_level == "START_SCREEN":
            self.level = Start()
        elif next_level == "GAME_OVER":
            self.level = GameOver()
        elif next_level == "NEXT_LEVEL":
            # self.level = Fase(1000, 500, "Astro Ape", "assets\\bg_space.png")
            self.level = Victory()
            pass
        return True

    def draw(self):
        self.level.draw()

        pygame.display.update()