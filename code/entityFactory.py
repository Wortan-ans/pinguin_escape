#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1a':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'level1a{i}', position=(0,0)))
                    list_bg.append(Background(f'level1a{i}', position=(576, 0)))
                return list_bg
            case 'level2a':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'level2a{i}', position=(0, 0)))
                    list_bg.append(Background(f'level2a{i}', position=(576, 0)))
                return list_bg
            case 'level3a':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'level3a{i}', position=(0, 0)))
                    list_bg.append(Background(f'level3a{i}', position=(576, 0)))
                return list_bg
            case 'player':
                return Player(name='player', position=(10,162))
            case 'rat':
                return Enemy(name='rat', position=(600, random.randint(0,220)))
            case 'rat1':
                return Enemy(name='rat1', position=(600, random.randint(0,220)))
            case 'rat2':
                return Enemy(name='rat2', position=(600, random.randint(0,220)))
        return None
