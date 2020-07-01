import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from treasure import Treasure


class Spell(Treasure):
    def set_for_player(self, player):
        player.learn(self)

    def __str__(self):
        return 'Spell: ' + self.name + ': damage: ' + str(self.damage) + ', cost: ' +\
               str(self.mana_cost) + ', range: ' + str(self.cast_range)
