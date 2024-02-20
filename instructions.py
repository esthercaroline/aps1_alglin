import pygame

class Instructions():
    def __init__(self):
        bg_image = pygame.image.load("assets\\bg_space.png")
        self.bg = pygame.transform.scale(bg_image, (1000, 500))

        font_title = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 80)
        self.text_font = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 20)

        self.instructions = font_title.render('Instruções', True, (0, 102, 204))

        self.play_text = "Jogar"
        self.play = self.text_font.render(self.play_text, True, (0, 102, 204))  # Azul escuro
        self.play_padding = 10  # Espaçamento interno
        self.play_rect = self.play.get_rect(center=(700, 450))
        self.play_surface = pygame.Surface((self.play_rect.width + 2 * self.play_padding, self.play_rect.height + 2 * self.play_padding), pygame.SRCALPHA)
        self.play_surface.fill((255, 255, 255, 100))  # Transparente
        self.play_rect = self.play_surface.get_rect(center=(700, 450))
        self.play_rect_text = self.play.get_rect(center=self.play_surface.get_rect().center)

        self.back_text = "Back"
        self.back = self.text_font.render(self.back_text, True, (0, 102, 204))  # Azul escuro
        self.back_padding = 10  # Espaçamento interno
        self.back_rect = self.back.get_rect(center=(300, 450))
        self.back_surface = pygame.Surface((self.back_rect.width + 2 * self.back_padding, self.back_rect.height + 2 * self.back_padding), pygame.SRCALPHA)
        self.back_surface.fill((255, 255, 255, 100))  # Transparente
        self.back_rect = self.back_surface.get_rect(center=(300, 450))
        self.back_rect_text = self.back.get_rect(center=self.back_surface.get_rect().center)

        self.screen = pygame.display.set_mode((1000, 500))

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg, (0, 0))

        self.screen.blit(self.instructions, self.instructions.get_rect(center=(1000/2, 100)))

        i1 = self.text_font.render("1. Use o mouse para mirar e clicar para lançar o macaco.", True, (173, 216, 230))
        self.screen.blit(i1, (80, 180))
        i2 = self.text_font.render("2. Evite que o macaco atinja o chão ou ultrapasse a tela.", True, (173, 216, 230))
        self.screen.blit(i2, (80, 230)) 
        i3 = self.text_font.render("3. Desvie das bananas! Elas tiram uma vida a cada colisão.", True, (173, 216, 230))
        self.screen.blit(i3, (80, 280)) 
        i4 = self.text_font.render("4. Clique na seta para iniciar o jogo.", True, (173, 216, 230))
        self.screen.blit(i4, (80, 330))

        self.screen.blit(self.play_surface, self.play_rect)
        self.play_rect_text.center = self.play_rect.center
        self.screen.blit(self.play, self.play_rect_text)

        self.screen.blit(self.back_surface, self.back_rect)
        self.back_rect_text.center = self.back_rect.center
        self.screen.blit(self.back, self.back_rect_text)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_rect.collidepoint(event.pos):
                    return "GAME_SCREEN"
                elif self.back_rect.collidepoint(event.pos):
                    return "START_SCREEN"
