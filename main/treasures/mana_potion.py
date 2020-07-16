import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from treasure import Treasure

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import MANA_POTION_STR_REPRESENTATION_CLASS_NAME, MANA_POTION_STR_REPRESENTATION_MANA_FIELD


class ManaPotion(Treasure):
    def set_for_player(self, player):
        player.take_mana(int(self.mana_regeneration))

    def __str__(self):
        return MANA_POTION_STR_REPRESENTATION_CLASS_NAME + self.name +\
            MANA_POTION_STR_REPRESENTATION_MANA_FIELD + str(self.mana_regeneration)
