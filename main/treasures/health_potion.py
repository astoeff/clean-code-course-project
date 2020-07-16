import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from treasure import Treasure

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import HEALTH_POTION_STR_REPRESENTATION_CLASS_NAME, HEALTH_POTION_STR_REPRESENTATION_HEALING_FIELD


class HealthPotion(Treasure):
    def set_for_player(self, player):
        player.take_healing(int(self.healing))

    def __str__(self):
        return HEALTH_POTION_STR_REPRESENTATION_CLASS_NAME + self.name +\
            HEALTH_POTION_STR_REPRESENTATION_HEALING_FIELD + str(self.healing)
