import pygame

class Inicio():
    def __init__(self):
        self.running = True

        bg_image = pygame.image.load("assets\\bg_space.png")
        self.bg = pygame.transform.scale(bg_image, (1280, 720))

        font = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 100)
        self.game_title = font.render("Astro Ape", True, (211, 177, 110))
        self.font_text = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 60)

        self.button_rect_play = pygame.Rect(515, 315, 250, 80)

        self.play = self.font_text.render("Jogar", True, (174, 139, 71))
        self.play_rect = self.play.get_rect(center=(1280/2, 720/2))

        self.button_rect_instruc = pygame.Rect(445, 455, 390, 80)

        self.instructions  = self.font_text.render("Instruções", True, (174, 139, 71))
        self.instrucions_rect = self.instructions .get_rect(center=(1280/2, 500))

        self.screen = pygame.display.set_mode((1000, 500))

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.game_title, (220, 130))

        pygame.draw.rect(self.screen, (240, 229, 198), self.button_rect_play)

        self.screen.blit(self.play, self.play_rect)

        pygame.draw.rect(self.screen, (240, 229, 198), self.button_rect_instruc)

        self.screen.blit(self.instructions , self.instrucions_rect)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect_play.collidepoint(event.pos):
                    return "GAME_SCREEN"
                elif self.button_rect_instruc.collidepoint(event.pos):
                    return "INSTRUCTIONS_SCREEN"
                
                