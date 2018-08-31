import pygame


class Item(pygame.sprite.Sprite):

    def __init__(self, name, value):
        self.name = name
        self.value = value
