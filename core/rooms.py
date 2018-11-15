import os

from enum import Enum

import pygame

from gamesettings import GameSettings as gs


class Rooms(Enum):
    OPENING_BEACH_ROOM = 0
    SECOND_ROOM = 1


class Room(pygame.sprite.Sprite):

    def __init__(self, north, south, east, west, _id):
        super().__init__()
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.room_map = []
        self._id = _id

    def load_map(self):
        pass

    def render(self, screen):
        pass


class OpeningBeachRoom(Room):

    def __init__(self):
        super().__init__(Rooms.SECOND_ROOM, Rooms.SECOND_ROOM,
                         Rooms.SECOND_ROOM, Rooms.SECOND_ROOM,
                         Rooms.OPENING_BEACH_ROOM)

        self.room_map = []

    def load_map(self):
        map_file = os.path.join(gs.MAP, "opening_beach.txt")
        with open(map_file, "r") as room:
            for line in room:
                self.room_map.append(line)

    def render(self, screen):
        for y, line in enumerate(self.room_map):
            for x, column in enumerate(line):
                rect_x = x * gs.TILESIZE
                rect_y = y * gs.TILESIZE
                if column == "S":
                    pygame.draw.rect(screen, gs.SAND_YELLOW,
                                     (rect_x, rect_y,  32, 32))
                elif column == "W":
                    pygame.draw.rect(screen, gs.OCEAN_BLUE,
                                     (rect_x, rect_y,  32, 32))


class SecondRoom(Room):

    def __init__(self):
        super().__init__(Rooms.OPENING_BEACH_ROOM, Rooms.OPENING_BEACH_ROOM,
                         Rooms.OPENING_BEACH_ROOM, Rooms.OPENING_BEACH_ROOM,
                         Rooms.SECOND_ROOM)
