import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from playable import Playable

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import (KNOWN_AS_MIDDLE_PART_TEXT, HERO_INFORMATION_NAME_FIELD_TEXT,
                       HERO_INFORMATION_TITLE_FIELD_TEXT, HERO_INFORMATION_KNOWN_AS_FIELD_TEXT,
                       HERO_INFORMATION_HEALTH_FIELD_TEXT, HERO_INFORMATION_MANA_FIELD_TEXT,
                       HERO_INFORMATION_MANA_REGENERATION_RATE_FIELD_TEXT, HERO_INFORMATION_WEAPON_FIELD_TEXT,
                       HERO_INFORMATION_SPELL_FIELD_TEXT)


class Hero(Playable):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    @property
    def known_as(self):
        return self.name + KNOWN_AS_MIDDLE_PART_TEXT + self.title

    def print_hero_information(self):
        print(HERO_INFORMATION_NAME_FIELD_TEXT, self.name)
        print(HERO_INFORMATION_TITLE_FIELD_TEXT, self.title)
        print(HERO_INFORMATION_KNOWN_AS_FIELD_TEXT, self.known_as)
        print(HERO_INFORMATION_HEALTH_FIELD_TEXT, self.health)
        print(HERO_INFORMATION_MANA_FIELD_TEXT, self.mana)
        print(HERO_INFORMATION_MANA_REGENERATION_RATE_FIELD_TEXT, self.mana_regeneration_rate)
        print(HERO_INFORMATION_WEAPON_FIELD_TEXT, self.weapon)
        print(HERO_INFORMATION_SPELL_FIELD_TEXT, self.spell)
