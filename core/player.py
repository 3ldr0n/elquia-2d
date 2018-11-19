import os

import pygame

from gamesettings import GameSettings as gs


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.width = 32
        self.height = 64
        self.spritesheet = pygame.image.load(
            os.path.join(gs.ASSETS, "characters/main.png")).convert_alpha()
        self.set_idle_image(
            gs.SCREEN_BORDER, gs.SCREEN_HEIGHT - gs.SCREEN_BORDER)

        self.name = None
        self.hp = 100
        self.maxhp = 100
        self.mp = 100
        self.maxmp = 100
        self.inventory = []
        self.current_room = None
        self.speed = gs.TILESIZE / 5

    def set_current_room(self, room):
        self.current_room = room

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

        self.spritesheet.set_clip(pygame.Rect(
            16, 10*self.height, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_walking_up_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            16, 8*self.height, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_down_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            16, 10*self.height, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_right_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            16, 11*self.height, self.width, self.height))
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_left_image(self):
        self.spritesheet.set_clip(pygame.Rect(
            16, 9*self.height, self.width, self.height))
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

    def collide_with_tiles(self):
        for tile in self.game.collision_tile_group:
            if pygame.sprite.collide_rect(self, tile):
                return True

        return False

    def pass_to_other_room(self):
        for tile in self.game.trespassing_tile_group:
            if pygame.sprite.collide_rect(self, tile):
                return True

        return False

    def get_item(self, item):
        self.inventory.append(item)

    def handle_keys(self):
        """Handles user movement. """
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.set_walking_right_image()
            self.rect.x += self.speed
            if self.collide_with_tiles():
                self.rect.x -= self.speed

        if key[pygame.K_LEFT]:
            self.set_walking_left_image()
            self.rect.x -= self.speed
            if self.collide_with_tiles():
                self.rect.x += self.speed+2

        if key[pygame.K_UP]:
            self.set_walking_up_image()
            self.rect.y -= self.speed
            if self.collide_with_tiles():
                self.rect.y += self.speed

        if key[pygame.K_DOWN]:
            self.set_walking_down_image()
            self.rect.y += self.speed
            if self.collide_with_tiles():
                self.rect.y -= self.speed

        if 1 not in key:
            self.set_idle_image()

    def save_info(self):
        pass
