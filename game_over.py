import pygame 

class GameOver():
    def __init__(self):
        bg_image = pygame.image.load("assets\\bg_space.png")
        self.bg = pygame.transform.scale(bg_image, (1000, 500))

        font_title = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 100)
        self.game_title = font_title.render("GAME-OVER", True, (0, 102, 204))  # Azul escuro
        title_rect = self.game_title.get_rect(center=(1000/2, 100))


        self.loser_text = "Você não resistiu a tentação das bananas e falhou em chegar ao planeta dos macacos!"
        font_loser = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 15)
        self.loser = font_loser.render(self.loser_text, True, (255, 255, 255))


        font_button = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 40)
        self.restart_text = "Reiniciar"
        self.restart = font_button.render(self.restart_text, True, (0, 102, 204))  # Azul escuro
        self.restart_padding = 10  # Espaçamento interno
        self.restart_rect = self.restart.get_rect(center=(1000/2, 350))
        self.restart_surface = pygame.Surface((self.restart_rect.width + 2 * self.restart_padding, self.restart_rect.height + 2 * self.restart_padding), pygame.SRCALPHA)
        self.restart_surface.fill((255, 255, 255, 100))  # Transparente
        self.restart_rect = self.restart_surface.get_rect(center=(1000/2, 350))
        self.restart_rect_text = self.restart.get_rect(center=self.restart_surface.get_rect().center)

        self.quit_text = "Sair"
        self.quit = font_button.render(self.quit_text, True, (0, 102, 204))  # Azul escuro
        self.quit_padding = 10  # Espaçamento interno
        self.quit_rect = self.quit.get_rect(center=(1000/2, 450))
        self.quit_surface = pygame.Surface((self.quit_rect.width + 2 * self.quit_padding, self.quit_rect.height + 2 * self.quit_padding), pygame.SRCALPHA)
        self.quit_surface.fill((255, 255, 255, 100))  # Transparente
        self.quit_rect = self.quit_surface.get_rect(center=(1000/2, 450))
        self.quit_rect_text = self.quit.get_rect(center=self.quit_surface.get_rect().center)

        self.screen = pygame.display.set_mode((1000, 500))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.game_title, self.game_title.get_rect(center=(1000/2, 100)))
        self.screen.blit(self.restart_surface, self.restart_rect)
        self.restart_rect_text.center = self.restart_rect.center
        self.screen.blit(self.restart, self.restart_rect_text)
        self.screen.blit(self.quit_surface, self.quit_rect)
        self.quit_rect_text.center = self.quit_rect.center
        self.screen.blit(self.quit, self.quit_rect_text)
        self.screen.blit(self.loser, self.loser.get_rect(center=(1000/2, 200)))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart_rect.collidepoint(event.pos):
                    return "GAME_SCREEN"
                elif self.quit_rect.collidepoint(event.pos):
                    return -1
