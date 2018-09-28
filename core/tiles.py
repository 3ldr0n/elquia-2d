import pygame

from gamesettings import GameSettings as gs


class Grass(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        self.group = group
        super().__init__(self.group)
        self.image = pygame.Surface((gs.TILESIZE, gs.TILESIZE))
        self.image.fill(gs.WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * gs.TILESIZE
        self.rect.y = self.y * gs.TILESIZE
