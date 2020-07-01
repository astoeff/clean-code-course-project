import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from playable import Playable


class Hero(Playable):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    def __repr__(self):
        return "Hero(health={h}, mana={m})".format(h=self.health, m=self.mana)

    def known_as(self):
        return self.name + ' the ' + self.title

    def print_hero(self):
        print('Name: ', self.name)
        print('Title: ', self.title)
        print('Known as: ', self.known_as())
        print('Health: ', self.health)
        print('Mana: ', self.mana)
        print('Mana regeneration rate: ', self.mana_regeneration_rate)
        if self.weapon is not None:
            print('Weapon: ', str(self.weapon)[8:])
        else:
            print('Weapon: ', self.weapon)
        print('Spell: ', self.spell)
        print()
