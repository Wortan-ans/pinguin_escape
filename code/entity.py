#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.const import ENTITY_HP, ENTITY_DMG, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load("./asset/" + name + ".png").convert_alpha() # otimiza as imagens
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.hp = ENTITY_HP[self.name]
        self.dmg = ENTITY_DMG[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move( self):
        pass
