import os

from enum import Enum

import pygame

from gamesettings import GameSettings as gs


class Rooms(Enum):
    OPENING_ROOM = 0
    SECONDING_ROOM = 1


class Room(pygame.sprite.Sprite):

    def __init__(self, north, south, east, west, _id):
        super().__init__()
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.room_map = []
        self._id = _id


class OpeningRoom(Room):

    def __init__(self):
        super().__init__(Rooms.SECONDING_ROOM, Rooms.SECONDING_ROOM,
                         Rooms.SECONDING_ROOM, Rooms.SECONDING_ROOM,
                         Rooms.OPENING_ROOM)
        self.room_map = []

    def load_room(self):
        map_file = os.path.join(gs.MAP, "opening.txt")
        with open(map_file, "r") as room:
            for line in room:
                self.room_map.append(line)

    def render(self, screen):
        for line_, line in enumerate(self.room_map):
            for column_, column in enumerate(line):
                x = column_ * gs.TILESIZE
                y = line_ * gs.TILESIZE
                if column == "1":
                    pygame.draw.rect(screen, gs.WHITE, (x, y,  32, 32))


class SecondingRoom(Room):

    def __init__(self):
        super().__init__(Rooms.OPENING_ROOM, Rooms.OPENING_ROOM,
                         Rooms.OPENING_ROOM, Rooms.OPENING_ROOM)
