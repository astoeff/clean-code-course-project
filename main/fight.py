from constants import (DIRECTIONS_WITH_THEIR_OPPOSITES_DICTIONARY, FIGHT_INITIAL_INFORMATION_PART,
                       PLAYER_ZERO_DAMAGE_WHEN_ATTACKING, FIGHT_HERO_ATTACK_INFORMATION_PART,
                       FIGHT_HERO_CANNOT_ATTACK_INFORMATION_PART, FIGHT_ENEMY_ATTACK_INFORMATION_PART,
                       FIGHT_ENEMY_CANNOT_ATTACK_INFORMATION_PART)


class Fight:
    def __init__(self, hero, enemy, distance=0, direction=0):
        self.hero = hero
        self.enemy = enemy
        self.distance = distance
        self.direction = direction
        self.information_parts = [FIGHT_INITIAL_INFORMATION_PART + self.enemy]

    @property
    def oposite_direction(self):
        return DIRECTIONS_WITH_THEIR_OPPOSITES_DICTIONARY[self.direction]

    def hero_attack(self):
        damage_from_attack = self.hero.attack()
        can_hero_attack = damage_from_attack > PLAYER_ZERO_DAMAGE_WHEN_ATTACKING
        if can_hero_attack:
            self.information_parts.append(FIGHT_HERO_ATTACK_INFORMATION_PART + damage_from_attack)
        else:
            self.information_parts.append(FIGHT_HERO_CANNOT_ATTACK_INFORMATION_PART)
        self.enemy.take_damage(damage_from_attack)

    def enemy_attack(self):
        damage_from_attack = self.enemy.attack()
        can_enemy_attack = damage_from_attack > PLAYER_ZERO_DAMAGE_WHEN_ATTACKING
        if can_enemy_attack:
            self.information_parts.append(FIGHT_ENEMY_ATTACK_INFORMATION_PART + damage_from_attack)
        else:
            self.information_parts.append(FIGHT_ENEMY_CANNOT_ATTACK_INFORMATION_PART)
        self.hero.take_damage(damage_from_attack)

    def execute(self):
        is_fight_in_progress = self.hero.is_alive() and self.enemy.is_alive()
        while is_fight_in_progress:
            if self.hero.is_alive():
                self.hero_attack()
            if self.enemy.is_alive():
                self.enemy_attack()

    def get_fight_information(self):
        return self.information_parts
