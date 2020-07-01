import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from treasure import Treasure


class ManaPotion(Treasure):
    def set_for_player(self, player):
        player.take_mana(int(self.mana_regeneration))

    def __str__(self):
        return 'ManaPotion: ' + self.name + ': mana: ' + str(self.mana_regeneration)
