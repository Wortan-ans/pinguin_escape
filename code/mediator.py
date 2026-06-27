import pygame

from code.enemy import Enemy
from code.entity import Entity
from code.player import Player
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
    def __verify_collision_entity(ent1,ent2):
        valid_collision = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Shot):
            valid_collision = True
        elif isinstance(ent1, Shot) and isinstance(ent2, Enemy):
            valid_collision = True
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_collision = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_collision = True


        if valid_collision:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.hp -= ent2.dmg
                ent2.hp -= ent1.dmg
                ent1.last_dmg = ent2.last_dmg
                ent2.last_dmg = ent1.last_dmg

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'playershot' or 'player':
            for ent in entity_list:
                if ent.name == 'player':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            track_entity1 = entity_list[i]
            Mediator.__verify_collision_window(track_entity1)
            for j in range(i+1,len(entity_list)):
                track_entity2 = entity_list[j]
                Mediator.__verify_collision_entity(track_entity1,track_entity2)

    @staticmethod
    def verify_hp(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.hp <= 0:
                if isinstance(ent, Enemy):
                    Mediator.__give_score(ent, entity_list)
                entity_list.remove(ent)

