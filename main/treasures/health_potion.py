import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from treasure import Treasure


class HealthPotion(Treasure):
    def set_for_player(self, player):
        player.take_healing(int(self.healing))

    def __str__(self):
        return 'HealthPotion: ' + self.name + ': healing: ' + str(self.healing)
