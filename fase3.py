import numpy as np
import pygame
from pygame.locals import *
from monkey import Monkey

pygame.init()

class Fase3():
    def __init__(self, width, height, title, bg_path):
        # Initialize the game
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # Load the background
        self.background = pygame.image.load(bg_path)

        # Load the platform
        self.platform_rect = pygame.Rect((self.width - 200) // 2, (self.height - 400), 200, 20)
        self.platform_img = pygame.image.load("assets\platform.png")
        self.platform_img = pygame.transform.scale(self.platform_img, (150, 60))

        # Load the target planet
        self.target_rect = pygame.Rect(650, (self.height - 120), 90, 80)
        self.target_planet = pygame.image.load("assets\monkey_planet.png")
        self.target_planet = pygame.transform.scale(self.target_planet, (110, 100))

        # Load the speed bar
        self.speed_icon = pygame.image.load("assets\speed_icon.png")
        self.speed_icon = pygame.transform.scale(self.speed_icon, (20, 30))
        self.speed_text = "Velocidade"

        # Load the bananas
        self.banana_rect_one = pygame.Rect(330, (self.height - 340), 70, 60)
        self.banana_one = pygame.image.load("assets\double_banana.png")
        self.banana_one = pygame.transform.scale(self.banana_one, (70, 60))
        self.constant_banana_one = 5000
        self.banana_rect_two = pygame.Rect(600, (self.height - 250), 100, 100)
        self.banana_two = pygame.image.load("assets\penca.png")
        self.banana_two = pygame.transform.scale(self.banana_two, (80, 90))
        self.constant_banana_two = 7000

        # Load the hearts
        self.heart_image = pygame.image.load("assets\heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (20, 20))

        # Creates the monkey
        self.monkey = Monkey(self.platform_rect.centerx - 60, self.platform_rect.top - 60)

    def draw(self):
        # Draw everything on the screen
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.platform_img, (self.platform_rect.x, self.platform_rect.y))
        self.screen.blit(self.target_planet, (self.target_rect.x, self.target_rect.y))
        self.screen.blit(self.banana_one, (self.banana_rect_one.x, self.banana_rect_one.y))
        self.screen.blit(self.banana_two, (self.banana_rect_two.x, self.banana_rect_two.y))
        self.screen.blit(self.speed_icon, (8,470))
        font = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 12)
        text = font.render(self.speed_text, True, (255, 255, 255))
        self.screen.blit(text, (14, 450))
        self.monkey.draw()

        # Draw the hearts
        for i in range(self.monkey.lives):
            self.screen.blit(self.heart_image, (20 + i * 40, 20))

    def update(self):     
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.monkey.mouse_clicked = True

        # Collisions
        if self.monkey.monkey_rect.colliderect(self.target_rect):
            return "VICTORY"
        if self.monkey.position[0] == self.monkey.initial_pos[0] and self.monkey.position[1] == self.monkey.initial_pos[1]:	
            self.monkey.on_platform = True

        if self.monkey.position[1] > 500 or self.monkey.position[0] > 1000 or self.monkey.position[0] < 0 or self.monkey.position[1] < 0:
            if self.monkey.lives > 1:
                self.monkey.reset()
            elif self.monkey.lives == 1:
                return "GAME_OVER"

        if self.monkey.monkey_rect.colliderect(self.banana_rect_one) or self.monkey.monkey_rect.colliderect(self.banana_rect_two):
            if self.monkey.lives > 1:
                self.monkey.reset()
            elif self.monkey.lives == 1:
                return "GAME_OVER"

        self.monkey.update(np.array([self.banana_rect_one.x, self.banana_rect_one.y]), self.constant_banana_one, np.array([self.banana_rect_two.x, self.banana_rect_two.y]), self.constant_banana_two)