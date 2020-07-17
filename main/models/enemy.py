import random
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from playable import Playable

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import (ENEMY_MIN_MANA_AND_HEALTH_WHEN_INITIALISING, ENEMY_MAX_MANA_AND_HEALTH_WHEN_INITIALISING,
                       ENEMY_MIN_DAMAGE_WHEN_INITIALISING, ENEMY_MAX_DAMAGE_WHEN_INITIALISING, ENEMY_REPR_FIRST_PART,
                       ENEMY_REPR_HEALTH, ENEMY_REPR_MANA, ENEMY_REPR_DAMAGE)


class Enemy(Playable):
    def __init__(self):
        self.health = random.randint(ENEMY_MIN_MANA_AND_HEALTH_WHEN_INITIALISING,
                                     ENEMY_MAX_MANA_AND_HEALTH_WHEN_INITIALISING)
        self.mana = random.randint(ENEMY_MIN_MANA_AND_HEALTH_WHEN_INITIALISING,
                                   ENEMY_MAX_MANA_AND_HEALTH_WHEN_INITIALISING)
        self.damage = random.randint(ENEMY_MIN_DAMAGE_WHEN_INITIALISING, ENEMY_MAX_DAMAGE_WHEN_INITIALISING)
        self.weapon = None
        self.spell = None

    def attack(self):
        max_damage = max(self.damage, super().attack())
        return max_damage

    def __repr__(self):
        return ENEMY_REPR_FIRST_PART + ENEMY_REPR_HEALTH + str(self.health) + ENEMY_REPR_MANA + str(self.mana) +\
            ENEMY_REPR_DAMAGE + str(self.damage)
