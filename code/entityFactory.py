#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background

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
        return None
