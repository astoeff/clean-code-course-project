import random
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from playable import Playable

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import (ENEMY_MIN_MANA_AND_HEALTH_WHEN_INITIALISING, ENEMY_MAX_MANA_AND_HEALTH_WHEN_INITIALISING,
                       ENEMY_MIN_DAMAGE_WHEN_INITIALISING, ENEMY_MAX_DAMAGE_WHEN_INITIALISING)


class Enemy(Playable):
    def __init__(self):
        self.health = random.randint(ENEMY_MIN_MANA_AND_HEALTH_WHEN_INITIALISING,
                                     ENEMY_MAX_MANA_AND_HEALTH_WHEN_INITIALISING)
        self.mana = random.randint(ENEMY_MIN_MANA_AND_HEALTH_WHEN_INITIALISING,
                                   ENEMY_MAX_MANA_AND_HEALTH_WHEN_INITIALISING)
        self.damage = random.randint(ENEMY_MIN_DAMAGE_WHEN_INITIALISING, ENEMY_MAX_DAMAGE_WHEN_INITIALISING)

    def __repr__(self):
        return "Enemy(health={h},\
 mana={m}, damage={d})".format(h=self.health, m=self.mana, d=self.damage)
