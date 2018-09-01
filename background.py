import os

import pygame


class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(os.path.dirname(
            __file__), "assets/bricks.brown_.png")).convert()
        self.image.set_clip(pygame.Rect(0, 50, 50, 50))
        self.image = self.image.subsurface(self.image.get_clip())
