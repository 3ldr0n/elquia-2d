import os

import pygame

from gamesettings import GameSettings as gs


class Background(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            gs.ASSETS, "environment/wood_tileset.png")).convert()
        self.image.set_clip(pygame.Rect(0, 0, 90, 95))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
