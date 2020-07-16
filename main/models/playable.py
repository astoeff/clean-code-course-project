import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from constants import PLAYER_MIN_MANA_AND_HEALTH_VALUE, PLAYER_MAX_MANA_AND_HEALTH_VALUE

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


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
        return self.health > PLAYER_MIN_MANA_AND_HEALTH_VALUE

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

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def can_attack_with_weapon(self):
        return self.weapon is not None

    def can_cast_spell(self):
        does_playable_have_mana_for_casting_spell = False
        does_playable_have_spell = self.spell is not None
        if does_playable_have_spell:
            does_playable_have_mana_for_casting_spell = self.spell.mana_cost <= self.mana
        casting_spell_condition = does_playable_have_spell and does_playable_have_mana_for_casting_spell
        return casting_spell_condition

    def attack(self):
        weapon_damage = 0
        spell_damage = 0
        if self.can_attack_with_weapon():
            weapon_damage = self.weapon.damage
        if self.can_cast_spell():
            spell_damage = self.spell.damage
        max_damage = max(weapon_damage, spell_damage)
        return max_damage
