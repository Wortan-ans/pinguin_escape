#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top > 0:  #rect.top e bottom para delimitar a tela
            self.rect.centery -= 3/2
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom < 324:
            self.rect.centery += 3
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 4
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < 500:
            self.rect.centerx += 1
        pass
