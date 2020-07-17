import unittest
from main.utils import check_if_correct_key_is_pressed, check_is_row_and_column_inside_map


class TestUtils(unittest.TestCase):
    #check_if_correct_key_is_pressed()
    def test_with_given_correct_key_should_return_true(self):
        symbols = ['a', 'b']
        pressed = 'a'

        result = check_if_correct_key_is_pressed(symbols, pressed)
        expected = True

        self.assertEqual(expected, result)

    def test_with_given_incorrect_key_should_return_false(self):
        symbols = ['a', 'b']
        pressed = 'c'

        result = check_if_correct_key_is_pressed(symbols, pressed)
        expected = False

        self.assertEqual(expected, result)

    #check_is_row_and_column_inside_map()
    def test_with_given_row_and_column_inside_map(self):
        row = 0
        column = 1

        result = check_is_row_and_column_inside_map(row, column)
        expected = True

        self.assertEqual(expected, result)

    def test_with_given_row_inside_map_and_column_not_inside_map(self):
        row = 1
        column = -1

        result = check_is_row_and_column_inside_map(row, column)
        expected = False

        self.assertEqual(expected, result)

    def test_with_given_row_not_inside_map_and_column_inside_map(self):
        row = -1
        column = 2

        result = check_is_row_and_column_inside_map(row, column)
        expected = False

        self.assertEqual(expected, result)

    def test_with_given_row_not_inside_map_and_column_not_inside_map(self):
        row = -1
        column = -1

        result = check_is_row_and_column_inside_map(row, column)
        expected = False

        self.assertEqual(expected, result)
