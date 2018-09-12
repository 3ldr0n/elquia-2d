import os

import pygame

from gamesettings import GameSettings as gs


class Player(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.width = 32
        self.height = 64
        self.spritesheet = pygame.image.load(os.path.join(
            gs.ASSETS, "maleBase/full/advnt_full.png")).convert_alpha()
        self.set_idle_image(
            gs.SCREEN_BORDER, gs.SCREEN_HEIGHT - gs.SCREEN_BORDER)

        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.mp = 100
        self.maxmp = 100
        self.inventory = []

    def set_idle_image(self, x=None, y=None):
        """Set the player's idle image.

        :param x: x axis position.
        :param y: y axis position.
        """
        if x is None and y is None:
            x = self.rect.x
            y = self.rect.y

        self.spritesheet.set_clip(
            pygame.Rect(0, 0, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_walking_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            130, 0, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def is_alive(self):
        """Check if user is alive.

        :returns: Life bigger than zero.
        :rtype: bool

        """
        return self.hp > 0

    def get_item(self, item):
        self.inventory.append(item)

    def handle_keys(self):
        """Handles user movement. """
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.set_walking_image()
            self.rect.x += 5

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.set_walking_image()
            self.rect.x -= 5

        if key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]:
            self.set_walking_image()
            self.rect.y -= 5

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.set_walking_image()
            self.rect.y += 5

        if 1 not in key:
            self.set_idle_image()
