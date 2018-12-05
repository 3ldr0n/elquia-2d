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

        self.__walk_up_images = self.__set_walk_up_images()
        self.__walk_up_index = 0
        self.__walk_down_images = self.__set_walk_down_images()
        self.__walk_down_index = 0
        self.__walk_right_images = self.__set_walk_right_images()
        self.__walk_right_index = 0
        self.__walk_left_images = self.__set_walk_left_images()
        self.__walk_left_index = 0

        # Base values used to start the sprite rect object.
        self.set_idle_image(0, 0)

        self.name = None
        self.hp = 100
        self.maxhp = 100
        self.inventory = []
        self.current_room = None
        self.speed = gs.TILESIZE / 5

    def __set_walk_up_images(self):
        """Cuts all the necessary images for the walking up animation. """
        walk_up_images = []

        for i in range(9):
            self.spritesheet.set_clip(pygame.Rect(
                16+i*self.width, 8*self.height, self.width, self.height)),
            walk_up_image = self.spritesheet.subsurface(
                self.spritesheet.get_clip())
            walk_up_images.append(walk_up_image)

        return walk_up_images

    def __set_walk_down_images(self):
        """Cuts all the necessary images for the walking down animation. """
        walk_down_images = []

        for i in range(9):
            self.spritesheet.set_clip(pygame.Rect(
                16+i*self.width, 10*self.height, self.width, self.height)),
            walk_down_image = self.spritesheet.subsurface(
                self.spritesheet.get_clip())
            walk_down_images.append(walk_down_image)

        return walk_down_images

    def __set_walk_right_images(self):
        """Cuts all the necessary images for the walking right animation. """
        walk_right_images = []

        for i in range(9):
            self.spritesheet.set_clip(pygame.Rect(
                16+i*self.width, 11*self.height, self.width, self.height)),
            walk_right_image = self.spritesheet.subsurface(
                self.spritesheet.get_clip())
            walk_right_images.append(walk_right_image)

        return walk_right_images

    def __set_walk_left_images(self):
        """Cuts all the necessary images for the walking left animation. """
        walk_left_images = []

        for i in range(9):
            self.spritesheet.set_clip(pygame.Rect(
                16+i*self.width, 9*self.height, self.width, self.height)),
            walk_left_image = self.spritesheet.subsurface(
                self.spritesheet.get_clip())
            walk_left_images.append(walk_left_image)

        return walk_left_images

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

        self.image = self.__walk_down_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_walking_up_image(self):
        self.image = self.__walk_up_images[self.__walk_up_index]
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_down_image(self):
        self.image = self.__walk_down_images[self.__walk_down_index]
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_right_image(self):
        self.image = self.__walk_right_images[self.__walk_right_index]
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def set_walking_left_image(self):
        self.image = self.__walk_left_images[self.__walk_left_index]
        rect = self.image.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.rect = rect

    def __increment_walk_up_index(self):
        """Increments correctly the animation index, if the value is too
        high the methods sets the index back to zero.

        """
        self.__walk_up_index = (
            self.__walk_up_index + 1) % len(self.__walk_up_images)

    def __increment_walk_down_index(self):
        """Increments correctly the animation index, if the value is too
        high the methods sets the index back to zero.

        """
        self.__walk_down_index = (
            self.__walk_down_index + 1) % len(self.__walk_down_images)

    def __increment_walk_right_index(self):
        """Increments correctly the animation index, if the value is too
        high the methods sets the index back to zero.

        """
        self.__walk_right_index = (
            self.__walk_right_index + 1) % len(self.__walk_right_images)

    def __increment_walk_left_index(self):
        """Increments correctly the animation index, if the value is too
        high the methods sets the index back to zero.

        """
        self.__walk_left_index = (
            self.__walk_left_index + 1) % len(self.__walk_left_images)

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
        """Check if the user is colliding with any of the sprites loaded in the
        collision tiles group.

        """
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

    def update(self):
        """Handles user movement. """
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.__increment_walk_right_index()
            self.set_walking_right_image()
            self.rect.x += self.speed
            if self.collide_with_tiles():
                self.rect.x -= self.speed

        if key[pygame.K_LEFT]:
            self.__increment_walk_left_index()
            self.set_walking_left_image()
            self.rect.x -= self.speed
            if self.collide_with_tiles():
                self.rect.x += self.speed+2

        if key[pygame.K_UP]:
            self.__increment_walk_up_index()
            self.set_walking_up_image()
            self.rect.y -= self.speed
            if self.collide_with_tiles():
                self.rect.y += self.speed

        if key[pygame.K_DOWN]:
            self.__increment_walk_down_index()
            self.set_walking_down_image()
            self.rect.y += self.speed
            if self.collide_with_tiles():
                self.rect.y -= self.speed

        if 1 not in key:
            self.set_idle_image()

    def save_info(self):
        pass
