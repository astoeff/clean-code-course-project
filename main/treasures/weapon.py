import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from treasure import Treasure

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import WEAPON_STR_REPRESENTATION_CLASS_NAME, WEAPON_STR_REPRESENTATION_DAMAGE_FIELD


class Weapon(Treasure):
    def set_for_player(self, player):
        player.equip(self)

    def __str__(self):
        return WEAPON_STR_REPRESENTATION_CLASS_NAME + self.name +\
            WEAPON_STR_REPRESENTATION_DAMAGE_FIELD + str(self.damage)
