import os

import pygame

from gamesettings import GameSettings as gs


class Enemy(pygame.sprite.Sprite):

    def __init__(self, damage, items, image):
        self.damage = damage
        self.items = items
        self.spritesheet = pygame.image.load(os.path.join(gs.ASSETS, image))
