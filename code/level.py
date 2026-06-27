#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.player import Player
from code.const import EVENT_ENEMY
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.mediator import Mediator


class Level:
    def __init__(self,window, name,game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] =[]
        self.entity_list.extend(EntityFactory.get_entity('level1a'))
        self.entity_list.append(EntityFactory.get_entity('player')) #append é por causa de uma entidade
        self.timeout: int = 90000  # milisegundos, 90 segundos
        pygame.time.set_timer(EVENT_ENEMY, 1500)

    def run(self):
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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() #funciona igual ao quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('rat', 'rat1', 'rat2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(15, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',text_color=(160, 32, 240),text_pos= (10, 5))
            self.level_text(15, f'fps: {clock.get_fps():.0f}', text_color=(160, 32, 240),text_pos= (10, 305))
            pygame.display.flip()

            Mediator.verify_collision(entity_list=self.entity_list)
            Mediator.verify_hp(entity_list=self.entity_list)
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
