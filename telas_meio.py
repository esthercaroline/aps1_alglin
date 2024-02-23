import pygame

import pygame

class TelaMeio1():
    def __init__(self):
        # Initialize the game
        pygame.init()
        self.time_passed = 0
        self.total_time = 200000
        self.screen = pygame.display.set_mode((1000, 500))
        self.text = "Nível 1"

    def update(self):
        # Event handling and screen update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        # Update the time passed
        self.time_passed += pygame.time.get_ticks()
        if self.time_passed >= self.total_time:
            return "GAME_SCREEN"

    def draw(self):
        bg_img = pygame.image.load('assets/bg_space.png')
        bg_img = pygame.transform.scale(bg_img, (1000, 500))
        font = pygame.font.Font("assets/BruceForeverRegular-X3jd2.ttf", 100)  
        text = font.render(self.text, True, (255,255,255))
        self.screen.blit(bg_img, (0, 0))
        self.screen.blit(text, text.get_rect(center=(1000/2, 250)))

class TelaMeio2():
    def __init__(self):
        pygame.init()
        self.time_passed = 0
        self.total_time = 200000
        self.screen = pygame.display.set_mode((1000, 500))
        self.text = "Nível 2"

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        self.time_passed += pygame.time.get_ticks()
        if self.time_passed >= self.total_time:
            return "FASE2"

    def draw(self):
        bg_img = pygame.image.load('assets\orange_bg.png')
        bg_img = pygame.transform.scale(bg_img, (1000, 500))
        font = pygame.font.Font("assets/BruceForeverRegular-X3jd2.ttf", 100)  
        text = font.render(self.text, True, (255, 255, 255))
        self.screen.blit(bg_img, (0, 0))
        self.screen.blit(text, text.get_rect(center=(1000/2, 250)))

class TelaMeio3():
    def __init__(self):
        pygame.init()
        self.time_passed = 0
        self.total_time = 200000
        self.screen = pygame.display.set_mode((1000, 500))
        self.text = "Nível 3"

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        self.time_passed += pygame.time.get_ticks()
        if self.time_passed >= self.total_time:
            return "FASE3"

    def draw(self):
        bg_img = pygame.image.load('assets/green_bg.png')
        bg_img = pygame.transform.scale(bg_img, (1000, 500))
        font = pygame.font.Font("assets/BruceForeverRegular-X3jd2.ttf", 100) 
        text = font.render(self.texto, True, (255, 255, 255))
        self.screen.blit(bg_img, (0, 0))
        self.screen.blit(text, text.get_rect(center=(1000/2, 250)))
