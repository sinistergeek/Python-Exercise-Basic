from numbers import Number
from typing import Callable, Iterator

Num_Conv = Callable[[str],Number]

def numbers_from_rows(conversion: Num_Conv,text:str) -> Iterator[Number]:
    return(conversion(value) 
           for line in text.splitlines()
           for value in line.split())

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
