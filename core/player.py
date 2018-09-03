import os

import pygame

from gamesettings import GameSettings as gs


class Player(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.width = gs.SCREEN_HEIGHT * (10/100)
        self.height = 65
        self.set_idle_image(0, gs.SCREEN_HEIGHT -
                            self.height - gs.GROUND_HEIGHT)

        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.mp = 100
        self.maxmp = 100
        self.inventory = []
        self.standing = True
        self.jumping = False
        self.walking = False
        self.jump_height = 40
        # Calculates the max jump height on screen.
        self.max_jump_height = (gs.SCREEN_HEIGHT - self.height -
                                gs.GROUND_HEIGHT - self.jump_height)

    def set_idle_image(self, x=None, y=None):
        if x is None and y is None:
            x = self.rect.x
            y = self.rect.y

        self.image = pygame.image.load(os.path.join(
            gs.ASSETS, "maleBase/full/advnt_full.png")).convert_alpha()
        self.image.set_clip(pygame.Rect(
            0, 0, 30, 65))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_walking_image(self):
        self.image = pygame.image.load(os.path.join(
            gs.ASSETS, "maleBase/full/advnt_full.png")).convert_alpha()

        self.image.set_clip(pygame.Rect(
            130, 0, 30, 65))
        self.image = self.image.subsurface(self.image.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def __set_jumping_image(self):
        self.image = pygame.image.load(os.path.join(
            gs.ASSETS, "maleBase/full/advnt_full.png")).convert_alpha()
        self.image.set_clip(pygame.Rect(225, 65, 30, 65))
        self.image = self.image.subsurface(self.image.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_falling_image(self):
        self.image = pygame.image.load(os.path.join(
            gs.ASSETS, "maleBase/full/advnt_full.png")).convert_alpha()
        self.image.set_clip(pygame.Rect(230, 260, 30, 65))
        self.image = self.image.subsurface(self.image.get_clip())
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def is_alive(self):
        return self.hp > 0

    def get_item(self, item):
        self.inventory.append(item)

    def is_on_ground(self):
        """Verifies if the player is on the ground. """
        if self.rect.y == gs.SCREEN_HEIGHT - self.height - gs.GROUND_HEIGHT:
            self.standing = True
            self.jumping = False
            return True

        return False

    def __jump(self):
        if self.rect.y > self.max_jump_height and self.jumping is False:
            self.standing = False
            self.jumping = True
            self.__set_jumping_image()
            self.rect.y -= 40

    def handle_keys(self):
        """Handles user movement. """
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.walking = True
            self.set_walking_image()
            self.rect.x += 5

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 5

        if key[pygame.K_SPACE] or key[pygame.K_UP] or key[pygame.K_w]:
            self.__jump()

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            if self.is_on_ground():
                self.standing = True
                self.jumping = False
            else:
                self.rect.y += 10

        if 1 not in key:
            self.set_idle_image()
