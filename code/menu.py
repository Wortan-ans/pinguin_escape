#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.const import MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/menuBG.png")
        self.rect = self.surf.get_rect() #left=0 top=0 é o padrão


    def run(self):
        pygame.mixer_music.load('./asset/menusong.flac') # carregar a música
        pygame.mixer_music.play(-1)  #-1 para a música entrar em loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=70, text= 'Penguin', text_color=(176,205,223),text_center_pos=(444,80))
            self.menu_text(text_size=50, text='VS', text_color=(152, 166, 176), text_center_pos=(444, 145))
            self.menu_text(text_size=70, text='Rats', text_color=(128, 128, 128), text_center_pos=(444, 205))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=40, text=MENU_OPTION[i], text_color=(255, 255, 255), text_center_pos=(444,360+50*i))

            pygame.display.flip()

            #check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)