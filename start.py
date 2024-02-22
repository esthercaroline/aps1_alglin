import pygame

class Start():
    def __init__(self):
        bg_image = pygame.image.load("assets\\bg_space.png")
        self.bg = pygame.transform.scale(bg_image, (1000, 500))

        font_title = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 100)
        self.game_title = font_title.render("Astro Ape", True, (0, 102, 204))  # Azul escuro
        title_rect = self.game_title.get_rect(center=(1000/2, 100))

        font_button = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 40)
        self.play_text = "Jogar"
        self.play = font_button.render(self.play_text, True, (0, 102, 204))  # Azul escuro
        self.play_padding = 10  # Espaçamento interno
        self.play_rect = self.play.get_rect(center=(1000/2, 350))
        self.play_surface = pygame.Surface((self.play_rect.width + 2 * self.play_padding, self.play_rect.height + 2 * self.play_padding), pygame.SRCALPHA)
        self.play_surface.fill((255, 255, 255, 100))  # Transparente
        self.play_rect = self.play_surface.get_rect(center=(1000/2, 350))
        self.play_rect_text = self.play.get_rect(center=self.play_surface.get_rect().center)

        self.instructions_text = "Instruções"
        self.instructions = font_button.render(self.instructions_text, True, (0, 102, 204))  # Azul escuro
        self.instructions_padding = 10  # Espaçamento interno
        self.instructions_rect = self.instructions.get_rect(center=(1000/2, 450))
        self.instructions_surface = pygame.Surface((self.instructions_rect.width + 2 * self.instructions_padding, self.instructions_rect.height + 2 * self.instructions_padding), pygame.SRCALPHA)
        self.instructions_surface.fill((255, 255, 255, 100))  # Transparente
        self.instructions_rect = self.instructions_surface.get_rect(center=(1000/2, 450))
        self.instructions_rect_text = self.instructions.get_rect(center=self.instructions_surface.get_rect().center)

        self.screen = pygame.display.set_mode((1000, 500))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.game_title, self.game_title.get_rect(center=(1000/2, 100)))
        self.screen.blit(self.play_surface, self.play_rect)
        self.play_rect_text.center = self.play_rect.center
        self.screen.blit(self.play, self.play_rect_text)
        self.screen.blit(self.instructions_surface, self.instructions_rect)
        self.instructions_rect_text.center = self.instructions_rect.center
        self.screen.blit(self.instructions, self.instructions_rect_text)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_rect.collidepoint(event.pos):
                    return "TELA_MEIO1"
                elif self.instructions_rect.collidepoint(event.pos):
                    return "INSTRUCTIONS_SCREEN"
