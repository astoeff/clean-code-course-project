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
        self.information_parts = [FIGHT_INITIAL_INFORMATION_PART + str(self.enemy)]

    @property
    def oposite_direction(self):
        return DIRECTIONS_WITH_THEIR_OPPOSITES_DICTIONARY[self.direction]

    def set_information_parts(self, part_to_append):
        self.information_parts.append(part_to_append)

    def hero_attack(self):
        damage_from_attack = self.hero.attack()
        information_part_to_append = FIGHT_HERO_ATTACK_INFORMATION_PART + str(damage_from_attack)
        hero_can_not_attack = damage_from_attack == PLAYER_ZERO_DAMAGE_WHEN_ATTACKING
        if hero_can_not_attack:
            information_part_to_append = FIGHT_HERO_CANNOT_ATTACK_INFORMATION_PART
        self.set_information_parts(information_part_to_append)
        self.enemy.take_damage(damage_from_attack)

    def enemy_attack(self):
        damage_from_attack = self.enemy.attack()
        information_part_to_append = FIGHT_ENEMY_ATTACK_INFORMATION_PART + str(damage_from_attack)
        enemy_can_not_attack = damage_from_attack == PLAYER_ZERO_DAMAGE_WHEN_ATTACKING
        if enemy_can_not_attack:
            information_part_to_append = FIGHT_ENEMY_CANNOT_ATTACK_INFORMATION_PART
        self.set_information_parts(information_part_to_append)
        self.hero.take_damage(damage_from_attack)

    def execute(self):
        is_fight_in_progress = self.hero.is_alive() and self.enemy.is_alive()
        while is_fight_in_progress:
            if self.hero.is_alive():
                self.hero_attack()
            if self.enemy.is_alive():
                self.enemy_attack()
            is_fight_in_progress = self.hero.is_alive() and self.enemy.is_alive()

    def get_fight_information(self):
        return self.information_parts
