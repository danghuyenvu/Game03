"""
    Fire gate object
"""
import pygame
from pygame.locals import *
from settings import *
from utils import *
from build import *
import random

class FireGate:
    def __init__(self, pos, loader):
        self._pos = pygame.Vector2(pos)
        self.animation = self._loader.get_animation("huda_fire")
        self._rect = self._image.get_rect(center=self._pos)

    def check_magamata(self, player):
        if player.get_fire():
            return
        else:
            player.take_damage(25, self._pos)