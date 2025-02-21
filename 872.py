import pygame

class Ship:

    def __init__(self,ai_game):

        """Initalize the ship and set its starting position."""
        self.screen = ai_green.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)
