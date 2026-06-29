#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.constants import K_RETURN, K_BACKSPACE, KEYDOWN
from pygame.font import Font

from code.DBproxy import DBProxy
from code.const import SCORE_POS, MENU_OPTION

cs= (255, 255, 255)



class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load("./asset/menuBG.png").convert_alpha()
        self.rect = self.surf.get_rect()
        pass

    def save_score(self, menu_return:int, player_score:list[int]):
        db_proxy= DBProxy('dbscore')
        name= ''
        score = player_score[0]
        text = 'Enter your name (4 characters):'

        while True:
            self.window.blit(self.surf, dest=self.rect)
            self.score_text(45, text= 'CONGRATULATIONS!', text_color=cs, text_center_pos=SCORE_POS['Title'])
            self.score_text(20, text,text_color= cs, text_center_pos=SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name':name, 'score':score, 'date': get_formatted_date()})
                        self.show_score()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name +=event.unicode
            self.score_text(40, name, cs,SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show_score(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE',cs, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', cs, SCORE_POS['Label'])
        db_proxy = DBProxy('dbscore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_,name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', cs,SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        return

            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
