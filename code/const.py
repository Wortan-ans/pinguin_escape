import random

import pygame

MENU_OPTION = ( 'NEW GAME', 'SCORE', 'EXIT')
ENTITY_SPEED = {
    'level1a0':0,
    'level1a1':1,
    'level1a2':2,
    'level1a3':3,
    'level2a0': 0,
    'level2a1': 1,
    'level2a2': 2,
    'level2a3': 3,
    'level3a0': 0,
    'level3a1': 1,
    'level3a2': 2,
    'level3a3': 3,
    'rat': 3,
    'rat1': 4,
    'rat2': 5,
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_HP ={
    'level1a0':6545,
    'level1a1':5644,
    'level1a2':6445,
    'level1a3':8989,
    'level2a0': 6545,
    'level2a1': 5644,
    'level2a2': 6445,
    'level2a3': 8989,
    'level3a0': 6545,
    'level3a1': 5644,
    'level3a2': 6445,
    'level3a3': 8989,
    'rat': 50,
    'rat1': 20,
    'rat2': 10,
    'player': 150,
    'playershot': 1,
}

ENTITY_DMG = {
    'level1a0':0,
    'level1a1':0,
    'level1a2':0,
    'level1a3':0,
    'level2a0': 0,
    'level2a1': 0,
    'level2a2': 0,
    'level2a3': 0,
    'level3a0': 0,
    'level3a1': 0,
    'level3a2': 0,
    'level3a3': 0,
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
    'level2a0': 0,
    'level2a1': 0,
    'level2a2': 0,
    'level2a3': 0,
    'level3a0': 0,
    'level3a1': 0,
    'level3a2': 0,
    'level3a3': 0,
    'playershot':0,
    'player':0,
    'rat':10,
    'rat1':5,
    'rat2':5,
}

SCORE_POS = {'Title': (288, 50),
             'EnterName': (288, 80),
             'Label': (288, 90),
             'Name': (288, 110),
             0: (288, 110),
             1: (288, 130),
             2: (288, 150),
             3: (288, 170),
             4: (288, 190),
             5: (288, 210),
             6: (288, 230),
             7: (288, 250),
             8: (288, 270),
             9: (288, 290),
             }