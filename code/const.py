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

ENTITY_HP ={
    'level1a0':6545,
    'level1a1':5644,
    'level1a2':6445,
    'level1a3':8989,
    'rat': 50,
    'rat1': 20,
    'rat2': 10,
    'player': 500,
    'playershot': 1,
}

ENTITY_DMG = {
    'level1a0':0,
    'level1a1':0,
    'level1a2':0,
    'level1a3':0,
    'rat': 1,
    'rat1': 2,
    'rat2': 3,
    'player': 1,
    'playershot': 10,
}

ENTITY_SCORE= {
    'level1a0':0,
    'level1a1':0,
    'level1a2':0,
    'level1a3':0,
    'playershot':0,
    'player':0,
    'rat':10,
    'rat1':5,
    'rat2':5,
}