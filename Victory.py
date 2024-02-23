import pygame

class Victory():
    def __init__(self):
        bg_image = pygame.image.load("assets\\bg_victory.jpg")
        self.bg = pygame.transform.scale(bg_image, (1000, 500))

        font_button = pygame.font.Font("assets\BruceForeverRegular-X3jd2.ttf", 35)
        button_width = 200  

        self.restart_text = "Reiniciar"
        self.restart = font_button.render(self.restart_text, True, (255, 255, 255)) 
        self.restart_padding = 10  
        self.restart_rect = self.restart.get_rect(center=(1000/2 - button_width/2 - self.restart_padding, 450))  

        self.quit_text = "Sair"
        self.quit = font_button.render(self.quit_text, True, (255, 255, 255)) 
        self.quit_padding = 10  
        self.quit_rect = self.quit.get_rect(center=(1000/2 + button_width/2 + self.quit_padding, 450))  
        self.yay = pygame.mixer.Sound("assets\yay-6120.mp3")
        self.yay.set_volume(1)
        self.yay.play()
        self.screen = pygame.display.set_mode((1000, 500))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.restart, self.restart_rect)
        self.screen.blit(self.quit, self.quit_rect)

    def update(self):
        # Event handling and screen update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart_rect.collidepoint(event.pos):
                    return "GAME_SCREEN"
                elif self.quit_rect.collidepoint(event.pos):
                    return -1
