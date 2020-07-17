import unittest
from main.models.hero import Hero
from main.models.enemy import Enemy
from main.fight import Fight
from main.treasures.weapon import Weapon
from main.constants import (FIGHT_INITIAL_INFORMATION_PART, FIGHT_HERO_CANNOT_ATTACK_INFORMATION_PART,
                            FIGHT_HERO_ATTACK_INFORMATION_PART, DEFAULT_WEAPON_NAME, DEFAULT_WEAPON_DAMAGE,
                            FIGHT_ENEMY_CANNOT_ATTACK_INFORMATION_PART, FIGHT_ENEMY_ATTACK_INFORMATION_PART)


class TestFight(unittest.TestCase):
    #__init__()
    def test_with_given_correct_arguments_should_initialise_correctly(self):
        hero = Hero('hero', 'bravest', 100, 100, 2)
        enemy = Enemy()

        fight = Fight(hero, enemy)

        expected_hero = hero
        expected_enemy = enemy
        expected_distance = 0
        expected_direction = 0
        expected_information_parts = [FIGHT_INITIAL_INFORMATION_PART + str(enemy)]

        self.assertEqual(expected_hero, fight.hero)
        self.assertEqual(expected_enemy, fight.enemy)
        self.assertEqual(expected_distance, fight.distance)
        self.assertEqual(expected_direction, fight.direction)
        self.assertEqual(expected_information_parts, fight.information_parts)

    #hero_attack()
    def test_when_hero_can_not_attack_should_set_correct_information_part_and_enemy_takes_zero_damage(self):
        hero = Hero('hero', 'bravest', 100, 100, 2)
        enemy = Enemy()
        enemy_health_before_attack = enemy.health
        fight = Fight(hero, enemy)

        fight.hero_attack()

        result_information_parts = fight.information_parts
        expected_information_parts = [FIGHT_INITIAL_INFORMATION_PART + str(enemy),
                                      FIGHT_HERO_CANNOT_ATTACK_INFORMATION_PART]

        self.assertEqual(enemy_health_before_attack, enemy.health)
        self.assertEqual(expected_information_parts, result_information_parts)

    def test_when_hero_can_attack_should_set_correct_information_part_and_enemy_takes_damage_from_attack(self):
        hero = Hero('hero', 'bravest', 100, 100, 2)
        default_weapon = Weapon(name=DEFAULT_WEAPON_NAME, damage=DEFAULT_WEAPON_DAMAGE)
        hero.equip(default_weapon)
        enemy = Enemy()
        initial_enemy_as_string = str(enemy)
        enemy_health_before_attack = enemy.health
        fight = Fight(hero, enemy)

        fight.hero_attack()

        result_enemy_health = fight.enemy.health
        expected_enemy_health = enemy_health_before_attack - default_weapon.damage
        result_information_parts = fight.information_parts
        expected_information_parts = [FIGHT_INITIAL_INFORMATION_PART + initial_enemy_as_string,
                                      FIGHT_HERO_ATTACK_INFORMATION_PART + str(default_weapon.damage)]

        self.assertEqual(expected_enemy_health, result_enemy_health)
        self.assertEqual(expected_information_parts, result_information_parts)

    #enemy_attack()
    def test_when_enemy_can_not_attack_should_set_correct_information_part_and_hero_takes_zero_damage(self):
        hero = Hero('hero', 'bravest', 100, 100, 2)
        enemy = Enemy()
        enemy.damage = 0
        fight = Fight(hero, enemy)
        hero_health_before_attack = hero.health

        fight.enemy_attack()

        result_information_parts = fight.information_parts
        expected_information_parts = [FIGHT_INITIAL_INFORMATION_PART + str(enemy),
                                      FIGHT_ENEMY_CANNOT_ATTACK_INFORMATION_PART]

        self.assertEqual(hero_health_before_attack, hero.health)
        self.assertEqual(expected_information_parts, result_information_parts)

    def test_when_enemy_can_attack_should_set_correct_information_part_and_hero_takes_damage_from_attack(self):
        hero = Hero('hero', 'bravest', 100, 100, 2)
        enemy = Enemy()
        fight = Fight(hero, enemy)
        hero_health_before_attack = hero.health

        fight.enemy_attack()

        result_hero_health = fight.hero.health
        expected_hero_health = hero_health_before_attack - enemy.damage
        result_information_parts = fight.information_parts
        expected_information_parts = [FIGHT_INITIAL_INFORMATION_PART + str(enemy),
                                      FIGHT_ENEMY_ATTACK_INFORMATION_PART + str(enemy.damage)]

        self.assertEqual(expected_hero_health, result_hero_health)
        self.assertEqual(expected_information_parts, result_information_parts)

    #execute()
    def test_with_hero_that_can_not_attack_should_stop_when_hero_is_dead(self):
        hero = Hero('hero', 'bravest', 100, 100, 2)
        enemy = Enemy()
        enemy.damage = hero.health
        fight = Fight(hero, enemy)

        fight.execute()

        result_hero_alive_status = hero.is_alive()
        expected_hero_alive_status = False
        result_enemy_alive_status = enemy.is_alive()
        expected_enemy_alive_status = True
        result_information_parts = fight.information_parts
        expected_information_parts = [FIGHT_INITIAL_INFORMATION_PART + str(enemy),
                                      FIGHT_HERO_CANNOT_ATTACK_INFORMATION_PART,
                                      FIGHT_ENEMY_ATTACK_INFORMATION_PART + str(enemy.damage)]

        self.assertEqual(expected_hero_alive_status, result_hero_alive_status)
        self.assertEqual(expected_enemy_alive_status, result_enemy_alive_status)
        self.assertEqual(expected_information_parts, result_information_parts)

    def test_with_hero_that_can_attack_and_enemy_that_can_not_should_stop_when_enemy_is_dead(self):
        hero = Hero('hero', 'bravest', 100, 100, 2)
        enemy = Enemy()
        weapon = Weapon(name=DEFAULT_WEAPON_NAME, damage=enemy.health)
        hero.equip(weapon)
        fight = Fight(hero, enemy)
        initial_enemy_as_string = str(enemy)

        fight.execute()

        result_hero_alive_status = hero.is_alive()
        expected_hero_alive_status = True
        result_enemy_alive_status = enemy.is_alive()
        expected_enemy_alive_status = False
        result_information_parts = fight.information_parts
        expected_information_parts = [FIGHT_INITIAL_INFORMATION_PART + initial_enemy_as_string,
                                      FIGHT_HERO_ATTACK_INFORMATION_PART + str(weapon.damage)]

        self.assertEqual(expected_hero_alive_status, result_hero_alive_status)
        self.assertEqual(expected_enemy_alive_status, result_enemy_alive_status)
        self.assertEqual(expected_information_parts, result_information_parts)
