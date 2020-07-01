import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from treasure import Treasure


class Weapon(Treasure):
    def set_for_player(self, player):
        player.equip(self)

    def __str__(self):
        return 'Weapon: ' + self.name + ': damage: ' + str(self.damage)
