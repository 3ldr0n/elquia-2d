import os

import pygame

from gamesettings import GameSettings as gs


class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            gs.ASSETS, "bulkhead-walls-files/bulkhead-wallsx3.png")).convert()
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
