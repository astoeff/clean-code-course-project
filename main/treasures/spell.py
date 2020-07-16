import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from treasure import Treasure

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import (SPELL_STR_REPRESENTATION_CLASS_NAME, SPELL_STR_REPRESENTATION_DAMAGE_FIELD,
                       SPELL_STR_REPRESENTATION_COST_FIELD, SPELL_STR_REPRESENTATION_RANGE_FIELD)


class Spell(Treasure):
    def set_for_player(self, player):
        player.learn(self)

    def __str__(self):
        return SPELL_STR_REPRESENTATION_CLASS_NAME + self.name + SPELL_STR_REPRESENTATION_DAMAGE_FIELD\
            + str(self.damage) + SPELL_STR_REPRESENTATION_COST_FIELD +\
            str(self.mana_cost) + SPELL_STR_REPRESENTATION_RANGE_FIELD + str(self.cast_range)
