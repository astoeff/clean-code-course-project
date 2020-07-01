import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import PLAYER_MIN_MANA_AND_HEALTH_VALUE, PLAYER_MAX_MANA_AND_HEALTH_VALUE


def regulate_player_attribute(attribute):
    attribute_to_return = attribute
    if attribute < PLAYER_MIN_MANA_AND_HEALTH_VALUE:
        attribute_to_return = PLAYER_MIN_MANA_AND_HEALTH_VALUE
    elif attribute > PLAYER_MAX_MANA_AND_HEALTH_VALUE:
        attribute_to_return = PLAYER_MAX_MANA_AND_HEALTH_VALUE
    return attribute_to_return


class Playable:
    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    def take_healing(self, healing_points):
        if self.is_alive():
            self.health += healing_points
            self.health = regulate_player_attribute(attribute=self.health)
            return True
        return False

    def take_damage(self, damage_points):
        self.health -= damage_points
        self.health = regulate_player_attribute(attribute=self.health)

    def take_mana(self, mana_points):
        self.mana += mana_points
        self.mana = regulate_player_attribute(attribute=self.mana)
