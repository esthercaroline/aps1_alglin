import pygame
from pygame.locals import *
import numpy as np

class Monkey():
    def __init__(self, x, y, width=1000, height=500, lives=5):
        # Initialize the monkey and its attributes
        self.initial_pos = np.array([x, y])
        self.initial_speed = np.array([10, -10])
        self.gravity = np.array([0, 0.03])
        self.screen = pygame.display.set_mode((width, height))
        self.image = pygame.transform.scale(pygame.image.load("assets\monkey.png"), (70, 70))
        self.monkey_rect = self.image.get_rect()
        self.speed = self.initial_speed
        self.position = self.initial_pos

        # States
        self.mouse_clicked = False
        self.on_platform = True  
        self.lives = lives

        # Bar attributes
        self.max_bar_length = 100  
        self.bar_color = (50, 219, 87)  
        self.bar_height = 10  
        self.bar_outline_color = (0, 0, 0) 

    def update(self, banana_pos_one, constant_one, banana_pos_two = 0, constant_two = 0):  
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
    
        if self.mouse_clicked and self.on_platform:
            mouse_pos = np.array(pygame.mouse.get_pos())
            direction = mouse_pos - self.position
            if np.linalg.norm(direction) != 0:
                direction = direction.astype(float) / np.linalg.norm(direction)

            # Calculates the speed of the monkey based on the distance from the mouse and vector direction
            distance = np.linalg.norm(mouse_pos - self.position)
            speed_multiplier = 1 + distance / 400  
            self.speed = direction * 5 * speed_multiplier
            self.mouse_clicked = False
            self.on_platform = False

            # Checks if the monkey is out of the screen
            if (self.position[1] < 0 or self.position[1] > 400) or (self.position[0] < 0 or self.position[0] > 900):
                self.initial_speed = pygame.mouse.get_pos() - self.initial_pos
                self.initial_speed = (self.initial_speed / np.linalg.norm(self.initial_speed)) * 5
                self.speed = self.initial_speed
                self.position = self.initial_pos

        if not self.on_platform:
            # Calculates the attraction force of the monkey to the bananas
            direction_to_banana_one = banana_pos_one - self.position
            direction_to_banana_two = banana_pos_two - self.position
            distance_to_banana_one = np.linalg.norm(direction_to_banana_one)
            distance_to_banana_two = np.linalg.norm(direction_to_banana_two)

            if distance_to_banana_one != 0 or distance_to_banana_two != 0:
                attraction_force_one = (constant_one / distance_to_banana_one**2) * (direction_to_banana_one / distance_to_banana_one)
                attraction_force_two = (constant_two / distance_to_banana_two**2) * (direction_to_banana_two / distance_to_banana_two)
                resultant_force = attraction_force_one + attraction_force_two
                self.speed += resultant_force

            self.speed += self.gravity
            self.monkey_rect.topleft = self.position
            self.position = self.position + self.speed

    def reset(self):
        # Resets the monkey's position and speed
        if self.lives > 1:
            self.lives -= 1 
            self.position = self.initial_pos
            self.speed = self.initial_speed
            self.mouse_clicked = False
            self.on_platform = True

    def draw(self):
        self.monkey_rect.topleft = self.position
        self.screen.blit(self.image, self.monkey_rect)

        if not self.on_platform:
            return 
        
        mouse_pos = np.array(pygame.mouse.get_pos())
        distance = np.linalg.norm(mouse_pos - self.position)
        bar_length = int(distance / 5) 
        bar_length = min(bar_length, self.max_bar_length)
        bar_x = 35
        bar_y = self.screen.get_height() - self.bar_height - 10

        pygame.draw.rect(self.screen, self.bar_outline_color, (bar_x, bar_y, self.max_bar_length, self.bar_height), 1)

        # Draw the speed bar
        pygame.draw.rect(self.screen, self.bar_color, (bar_x, bar_y, bar_length, self.bar_height))