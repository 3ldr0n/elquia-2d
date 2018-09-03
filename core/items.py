import pygame

from gamesettings import GameSettings as gs


class Item(pygame.sprite.Sprite):

    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value


class Weapon(Item):

    def __init__(self, name, value, damage, description):
        super().__init__(name, value)
        self.base_damage = damage
        self.description = description


class IronSword(Weapon):

    def __init__(self):
        super().__init__("Iron Sword", 10, 15, "Not so sharp")
