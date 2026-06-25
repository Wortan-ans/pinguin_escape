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
        menu_option = 0
        pygame.mixer_music.load('./asset/menusong.flac') # carregar a música
        pygame.mixer_music.play(-1)  #-1 para a música entrar em loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=46, text= 'Penguin', text_color=(176,205,223),text_center_pos=(288,52))
            self.menu_text(text_size=33, text='VS', text_color=(152, 166, 176), text_center_pos=(288, 94))
            self.menu_text(text_size=46, text='Rats', text_color=(128, 128, 128), text_center_pos=(288, 133))

            for i in range(len(MENU_OPTION)):
                if i==menu_option:
                    self.menu_text(text_size=26, text=MENU_OPTION[i], text_color=(160, 32, 240), text_center_pos=(288,234+32*i))
                else:
                    self.menu_text(text_size=26, text=MENU_OPTION[i], text_color=(255, 255, 255),text_center_pos=(288,234+32*i))
            #check events
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option = menu_option + 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option = menu_option - 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:   #enter
                        return MENU_OPTION[menu_option]




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)