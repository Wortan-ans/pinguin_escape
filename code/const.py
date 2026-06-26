import random

import pygame

MENU_OPTION = ( 'NEW GAME 1P', 'SCORE', 'EXIT')
ENTITY_SPEED = {
    'level1a0':0,
    'level1a1':1,
    'level1a2':2,
    'level1a3':3,
    'rat': 3,
    'rat1': 4,
    'rat2': 5,
}
EVENT_ENEMY = pygame.USEREVENT + 1