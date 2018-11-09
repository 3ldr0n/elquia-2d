import os

import pygame

from rooms import Rooms
from gamesettings import GameSettings as gs


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.width = 32
        self.height = 28
        self.spritesheet = pygame.image.load(
            os.path.join(gs.ASSETS, "Character Sheet.png")).convert_alpha()
        self.set_idle_image(
            gs.SCREEN_BORDER, gs.SCREEN_HEIGHT - gs.SCREEN_BORDER)

        self.name = None
        self.hp = 100
        self.maxhp = 100
        self.mp = 100
        self.maxmp = 100
        self.inventory = []
        self.current_room = Rooms.OPENING_ROOM
        self.speed = gs.TILESIZE / 5

    def set_name(self, name):
        self.name = name

    def set_idle_image(self, x=None, y=None):
        """Set the player's idle image.

        Parameters
        ----------
        x: int
            x axis position.
        y: int
            y axis position.
        """
        if x is None and y is None:
            x = self.rect.x
            y = self.rect.y

        self.spritesheet.set_clip(pygame.Rect(32, 0, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_walking_up_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            self.width, self.height+6, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_down_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            self.width, 0, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_right_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            self.width, 2*self.height+2*6, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_left_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            self.width, 3*self.height+3*6, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def is_alive(self):
        """Check if user is alive.

        Returns
        -------
        bool
            Life bigger than zero.

        """
        return self.hp > 0

    def check_border(self):
        if self.rect.x >= gs.SCREEN_WIDTH - self.width:
            self.rect.x = gs.SCREEN_WIDTH - self.width

        if self.rect.x <= gs.SCREEN_BORDER:
            self.rect.x = gs.SCREEN_BORDER

        if self.rect.y <= gs.SCREEN_BORDER:
            self.rect.y = gs.SCREEN_BORDER

        if self.rect.y + self.height > gs.SCREEN_HEIGHT - gs.SCREEN_BORDER:
            self.rect.y = gs.SCREEN_HEIGHT - self.height - gs.SCREEN_BORDER

    def get_item(self, item):
        self.inventory.append(item)

    def handle_keys(self):
        """Handles user movement. """
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.set_walking_right_image()
            self.rect.x += self.speed

        if key[pygame.K_LEFT]:
            self.set_walking_left_image()
            self.rect.x -= self.speed

        if key[pygame.K_UP]:
            self.set_walking_up_image()
            self.rect.y -= self.speed

        if key[pygame.K_DOWN]:
            self.set_walking_down_image()
            self.rect.y += self.speed

        if 1 not in key:
            self.set_idle_image()
