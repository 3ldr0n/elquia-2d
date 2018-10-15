import pygame

from gamesettings import GameSettings as gs


class Item(pygame.sprite.Sprite):

    def __init__(self, name, value, description):
        super().__init__()
        self.name = name
        self.value = value
        self.description = description


class Weapon(Item):

    def __init__(self, name, value, description, damage):
        super().__init__(name, value, description)
        self.base_damage = damage


class Inventory:
    pass
