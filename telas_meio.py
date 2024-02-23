import pygame

import pygame

class TelaMeio1():
    def __init__(self):
        # Initialize the game
        pygame.init()
        self.tempo_passado = 0
        self.tempo_total = 200000
        self.screen = pygame.display.set_mode((1000, 500))
        self.texto = "Nível 1"

    def update(self):
        # Event handling and screen update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        # Update the time passed
        self.tempo_passado += pygame.time.get_ticks()
        if self.tempo_passado >= self.tempo_total:
            return "GAME_SCREEN"

    def draw(self):
        imagem_fundo = pygame.image.load('assets/bg_space.png')
        imagem_fundo = pygame.transform.scale(imagem_fundo, (1000, 500))
        fonte = pygame.font.Font("assets/BruceForeverRegular-X3jd2.ttf", 100)  
        texto = fonte.render(self.texto, True, (255,255,255))
        self.screen.blit(imagem_fundo, (0, 0))
        self.screen.blit(texto, texto.get_rect(center=(1000/2, 250)))

class TelaMeio2():
    def __init__(self):
        pygame.init()
        self.tempo_passado = 0
        self.tempo_total = 200000
        self.screen = pygame.display.set_mode((1000, 500))
        self.texto = "Nível 2"

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        self.tempo_passado += pygame.time.get_ticks()
        if self.tempo_passado >= self.tempo_total:
            return "FASE2"

    def draw(self):
        imagem_fundo = pygame.image.load('assets\orange_bg.png')
        imagem_fundo = pygame.transform.scale(imagem_fundo, (1000, 500))
        fonte = pygame.font.Font("assets/BruceForeverRegular-X3jd2.ttf", 100)  # Corrigido o caminho da fonte
        texto = fonte.render(self.texto, True, (255, 255, 255))
        # Usando blit para desenhar o texto na tela
        self.screen.blit(imagem_fundo, (0, 0))
        self.screen.blit(texto, texto.get_rect(center=(1000/2, 250)))

class TelaMeio3():

    def __init__(self):
        pygame.init()
        self.tempo_passado = 0
        self.tempo_total = 200000
        self.screen = pygame.display.set_mode((1000, 500))
        self.texto = "Nível 3"

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        self.tempo_passado += pygame.time.get_ticks()
        if self.tempo_passado >= self.tempo_total:
            return "FASE3"

    def draw(self):
        imagem_fundo = pygame.image.load('assets/green_bg.png')
        imagem_fundo = pygame.transform.scale(imagem_fundo, (1000, 500))
        fonte = pygame.font.Font("assets/BruceForeverRegular-X3jd2.ttf", 100)  # Corrigido o caminho da fonte
        texto = fonte.render(self.texto, True, (255, 255, 255))
        # Usando blit para desenhar o texto na tela
        self.screen.blit(imagem_fundo, (0, 0))
        self.screen.blit(texto, texto.get_rect(center=(1000/2, 250)))
