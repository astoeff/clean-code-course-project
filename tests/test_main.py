import unittest
from main.models.hero import Hero
from main.treasures.weapon import Weapon
from main.constants import DEFAULT_WEAPON_NAME, DEFAULT_WEAPON_DAMAGE

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from . import equip_hero_with_default_weapon


class TestMain(unittest.TestCase):
    #equip_hero_with_default_weapon()
    def test_with_given_hero_should_equip_with_default_weapon(self):
        hero = Hero('hero', 'bravest', 100, 100, 2)

        result_equipped_hero = equip_hero_with_default_weapon(hero)
        result_equipped_weapon = result_equipped_hero.result_equipped_weapon
        expected_weapon = Weapon(name=DEFAULT_WEAPON_NAME, damage=DEFAULT_WEAPON_DAMAGE)

        self.assertEqual(expected_weapon, result_equipped_weapon)
