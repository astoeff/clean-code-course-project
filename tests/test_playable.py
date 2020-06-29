import unittest
from main.models.playable import Playable


class Player(Playable):
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        self.spell = None
        self.weapon = None


class TestPLayable(unittest.TestCase):
    #is_alive()
    def test_is_alive_with_given_alive_player_should_return_true(self):
        pl = Player(health=100, mana=50)

        result = pl.is_alive()
        expected = True

        self.assertEqual(expected, result)

    def test_is_alive_with_given_dead_player_should_return_false(self):
        pl = Player(health=0, mana=50)

        result = pl.is_alive()
        expected = False

        self.assertEqual(expected, result)

    #take_healing(healing_points)
    def test_take_healing_with_given_dead_player_should_return_false(self):
        pl = Player(health=0, mana=50)

        result = pl.take_healing(healing_points=20)
        expected = False

        self.assertEqual(expected, result)
        self.assertEqual(0, pl.health)

    def test_take_healing_with_given_alive_player_with_max_health_should_not_change_health_and_return_true(self):
        pl = Player(health=100, mana=50)

        result = pl.take_healing(healing_points=20)
        expected = True

        self.assertEqual(expected, result)
        self.assertEqual(100, pl.health)

    def test_take_healing_with_given_alive_player_with_less_than_max_health_should_change_health_and_return_true(self):
        pl = Player(health=90, mana=50)

        result = pl.take_healing(healing_points=20)
        expected = True

        self.assertEqual(expected, result)
        self.assertEqual(100, pl.health)

    #take_damage(damage_points)
    def test_with_given_dead_player_should_do_nothing(self):
        pl = Player(health=0, mana=50)

        pl.take_damage(damage_points=20)

        self.assertEqual(0, pl.health)

    def test_with_given_alive_player_and_points_more_than_health_should_change_health_to_zero(self):
        pl = Player(health=10, mana=50)

        pl.take_damage(damage_points=20)

        self.assertEqual(0, pl.health)

    def test_with_given_alive_player_and_points_less_than_health_should_change_health_correctly(self):
        pl = Player(health=30, mana=50)

        pl.take_damage(damage_points=20.2)

        self.assertEqual(9.8, pl.health)

    #take_mana(mana_points):
    def test_with_given_player_should_add_mana_points_to_mana(self):
        pl = Player(health=100, mana=50)

        pl.take_mana(mana_points=120)

        self.assertEqual(100, pl.mana)


if __name__ == '__main__':
    unittest.main()
