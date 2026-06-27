import pygame

from code.enemy import Enemy
from code.entity import Entity
from code.shot import Shot


class Mediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        #2xunderline significa que é um mét0do pr1vado a essa classe
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.hp = 0
        if isinstance(ent, Shot):
            if ent.rect.left >= 520:
                ent.hp = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            track_entity = entity_list[i]
            Mediator.__verify_collision_window(track_entity)

    @staticmethod
    def verify_hp(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.hp <= 0:
                entity_list.remove(ent)
