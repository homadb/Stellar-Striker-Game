import pygame

class Ship:

    def __init__(self, ss_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load image
        # rect means rectangle (the shape of image)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # ship position at start
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
