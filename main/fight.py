from constants import DIRECTIONS_WITH_THEIR_OPPOSITES_DICTIONARY, FIGHT_INITIAL_INFORMATION_PART


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
        pass

    def enemy_attack(self):
        pass

    def execute(self):
        pass
