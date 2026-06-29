#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.entity import Entity
from code.shot import Shot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 33

    def move(self):
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
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = 33
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_SPACE]:
                return Shot(name=f'{self.name}shot', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None

