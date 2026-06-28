#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import player
from code.player import Player
from code.const import EVENT_ENEMY, EVENT_TIMEOUT
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.mediator import Mediator

ct=(237, 33, 0)  # cor vermelha, hud, apenas para reduzir o tamanho

class Level:
    def __init__(self,window: Surface, name: str,menu_return, player_score:list[int]):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] =[]
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'a'))
        x = (EntityFactory.get_entity('player'))
        x.score = player_score[0]
        self.entity_list.append(x)
        self.timeout: int = 40000  # milisegundos, 90 segundos
        pygame.time.set_timer(EVENT_ENEMY, 1500)
        pygame.time.set_timer(EVENT_TIMEOUT, 100)

    def run(self, player_score:list[int]):
        clock = pygame.time.Clock()  # ajustar o FPS do jogo
        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest= ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot is not None:
                     self.entity_list.append(shoot)
                if ent.name == 'player':
                    self.level_text(15, f'Player -HP: {ent.hp}', text_color=ct,text_pos= (10, 25))
                    self.level_text(15, f'Score: {ent.score}', text_color=ct, text_pos=(10, 45))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() #funciona igual ao quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('rat', 'rat1', 'rat2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout <= 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'player':
                                player_score[0] = ent.score
                        return True

                #checar se o player ta vivo
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False


            self.level_text(15, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',text_color=ct,text_pos= (10, 5))
            self.level_text(15, f'fps: {clock.get_fps():.0f}', text_color=ct,text_pos= (10, 305))
            pygame.display.flip()

            Mediator.verify_collision(entity_list=self.entity_list)
            Mediator.verify_hp(entity_list=self.entity_list)
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
