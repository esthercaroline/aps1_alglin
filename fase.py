import numpy as np
import pygame
from pygame.locals import *
from monkey import Monkey

pygame.init()

class Fase():
    def __init__(self, width, height, title, bg_path):
        # Initialize the game
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # Load the background
        self.background = pygame.image.load(bg_path)
        self.background = pygame.transform.scale(self.background, (width, height))

        # Load the platform
        self.platform_rect = pygame.Rect(160, (self.height-90), 200, 20)
        self.platform_img = pygame.image.load("assets\platform.png")
        self.platform_img = pygame.transform.scale(self.platform_img, (150, 60))

        # Load the target planet
        self.target_rect = pygame.Rect(700, (self.height-300), 80, 80)
        self.target_planet = pygame.image.load("assets\planet_orange.png")
        self.target_planet = pygame.transform.scale(self.target_planet, (100, 100))

        # Load the speed bar
        self.speed_icon = pygame.image.load("assets\speed_icon.png")
        self.speed_icon = pygame.transform.scale(self.speed_icon, (20, 30))
        self.speed_text = "Velocidade"

        # Load the banana
        self.banana_rect = pygame.Rect(400, (self.height-400), 60, 80)
        self.banana = pygame.image.load("assets\solo_banana_png.png")
        self.banana = pygame.transform.scale(self.banana, (60, 80))
        self.constant_banana = 5000

        # Load the hearts
        self.heart_image = pygame.image.load("assets\heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (20, 20))
        
        # Creates the monkey
        self.monkey = Monkey(200, self.platform_rect.top - 60)

    def draw(self):
        # Draw everything on the screen
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.platform_img, (self.platform_rect.x, self.platform_rect.y))
        self.screen.blit(self.target_planet, (self.target_rect.x, self.target_rect.y))
        self.screen.blit(self.banana, (self.banana_rect.x, self.banana_rect.y))
        self.screen.blit(self.speed_icon, (8,470))
        font = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 12)
        text = font.render(self.speed_text, True, (255, 255, 255))
        self.screen.blit(text, (14, 450))

        # Draw the hearts
        for i in range(self.monkey.lives):
            self.screen.blit(self.heart_image, (20 + i * 40, 20))

        self.monkey.draw()

    def update(self):   
        # Event handling  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.monkey.mouse_clicked = True

        # Collisions  
        if self.monkey.monkey_rect.colliderect(self.target_rect):
            return "TELA_MEIO2"
        if self.monkey.position[0] == self.monkey.initial_pos[0] and self.monkey.position[1] == self.monkey.initial_pos[1]:	
            self.monkey.on_platform = True

        if self.monkey.position[1] > 500 or self.monkey.position[0] > 1000 or self.monkey.position[0] < 0 or self.monkey.position[1] < 0:
            if self.monkey.lives > 1:
                self.monkey.reset()
            elif self.monkey.lives == 1:
                return "GAME_OVER"

        if self.monkey.monkey_rect.colliderect(self.banana_rect):
            if self.monkey.lives > 1:
                self.monkey.reset()
            elif self.monkey.lives == 1:
                return "GAME_OVER"

        self.monkey.update(np.array([self.banana_rect.x, self.banana_rect.y]), self.constant_banana)