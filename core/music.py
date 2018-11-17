import os

import pygame

from gamesettings import GameSettings as gs


class Music:

    def __init__(self):
        self.ROOT_DIR = os.path.join(gs.ASSETS, "music/")
        pygame.mixer.init()

    def menu_song(self):
        song = os.path.join(
            self.ROOT_DIR, 'menu_theme.ogg')
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

    def background_song(self):
        song = os.path.join(
            self.ROOT_DIR, 'background_theme.ogg')
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

    def battle_song(self):
        song = os.path.join(
            self.ROOT_DIR, 'battle_theme.ogg')
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

    def ending_song(self):
        song = os.path.join(
            self.ROOT_DIR, 'ending_theme.ogg')
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
