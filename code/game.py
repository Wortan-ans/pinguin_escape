#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.level import Level
from code.const import MENU_OPTION
from code.menu import Menu
from code.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))

    def run(self):
        while True:
            score= Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                player_score = [0]
                level = Level(self.window, 'level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'level3', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save_score(menu_return, player_score)

            elif menu_return == MENU_OPTION[1]:
                score.show_score()

            elif menu_return == MENU_OPTION[2]: # parte do menu responsável por sair
                pygame.quit()
                quit()
            else:
                pygame.quit()
                quit()

