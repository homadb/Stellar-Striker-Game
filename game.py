import sys
from settings import Settings
import pygame

class StellarStriker:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stellar Striker")
        self.bg_color = (230, 230, 230)
        self.settings = Settings()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill(self.settings.bg_color)

if __name__ == '__main__':
    ss = StellarStriker()
    ss.run_game()