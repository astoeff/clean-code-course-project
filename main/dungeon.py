import sys
from copy import deepcopy
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from utils import validate_dungeon_map
from constants import (DUNGEON_MAP_STARTING_POSITION_SYMBOL, DUNGEON_MAP_HERO_POSITION_SYMBOL, DUNGEON_MAP_ROW_SEPARATOR,
                       UP_DIRECTION_STRING, DOWN_DIRECTION_STRING, LEFT_DIRECTION_STRING, RIGHT_DIRECTION_STRING,
                       DUNGEON_MAP_EMPTY_FIELD_POSITION_SYMBOL)


class Dungeon:
    def __init__(self, file):
        self.map = self.map_file_to_string(file)
        self.hero = None
        self.checkpoints = 0

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, m):
        if not hasattr(self, 'map'):
            validate_dungeon_map(m)
        self._map = m

    @property
    def map_as_list(self):
        map_as_list = []
        map_rows = self.map.split(DUNGEON_MAP_ROW_SEPARATOR)
        row_position = 0
        for row in map_rows:
            map_as_list.append([])
            for symbol in row:
                map_as_list[row_position].append(symbol)
            row_position += 1
        self._map_as_list = deepcopy(map_as_list)
        return self._map_as_list

    @map_as_list.setter
    def map_as_list(self, m):
        print(m)
        self.map = self.convert_map_as_list_to_string(m)
        self._map_as_list = deepcopy(m)
        print(self._map_as_list)

    def map_file_to_string(self, file):
        with open(file, 'r') as f:
            return f.read()

    def print_map(self):
        print(self.map)

    def spawn(self, hero):
        if DUNGEON_MAP_HERO_POSITION_SYMBOL in self.map:
            return False
        if DUNGEON_MAP_STARTING_POSITION_SYMBOL in self.map:
            self.hero = hero
            self.map = self.map.replace(DUNGEON_MAP_STARTING_POSITION_SYMBOL, DUNGEON_MAP_HERO_POSITION_SYMBOL, 1)
            return True

    def get_current_hero_position(self):
        hero_row = 0
        for row in self.map_as_list:
            hero_column = 0
            for symbol in row:
                if symbol == DUNGEON_MAP_HERO_POSITION_SYMBOL:
                    return hero_column, hero_row
                else:
                    hero_column += 1
            hero_row += 1
        return hero_column, hero_row

    def calculate_new_hero_position(self, movement_direction, hero_current_column, hero_current_row):
        hero_new_column = hero_current_column
        hero_new_row = hero_current_row

        if movement_direction == RIGHT_DIRECTION_STRING:
            hero_new_column = hero_current_column + 1
        elif movement_direction == LEFT_DIRECTION_STRING:
            hero_new_column = hero_current_column - 1
        elif movement_direction == UP_DIRECTION_STRING:
            hero_new_row = hero_current_row - 1
        elif movement_direction == DOWN_DIRECTION_STRING:
            hero_new_row = hero_current_row + 1
        return hero_new_column, hero_new_row

    def convert_map_as_list_to_string(self, map_as_list=None):
        if map_as_list:
            return DUNGEON_MAP_ROW_SEPARATOR.join(["".join(symbol) for symbol in map_as_list])
        return DUNGEON_MAP_ROW_SEPARATOR.join(["".join(symbol) for symbol in self.map_as_list])

    def update_hero_position_in_map_as_list(self, hero_current_column, hero_current_row, hero_new_column, hero_new_row):
        m = deepcopy(self.map_as_list)
        m[hero_current_row][hero_current_column] = DUNGEON_MAP_EMPTY_FIELD_POSITION_SYMBOL
        m[hero_new_row][hero_new_column] = DUNGEON_MAP_HERO_POSITION_SYMBOL
        self.map_as_list = deepcopy(m)
        self.map = self.convert_map_as_list_to_string()

    def move_hero(self, movement_direction):
        hero_current_column, hero_current_row = self.get_current_hero_position()
        hero_new_column, hero_new_row = self.calculate_new_hero_position(movement_direction, hero_current_column,
                                                                         hero_current_row)

        try:
            if self.map_as_list[hero_new_row][hero_new_column] == DUNGEON_MAP_EMPTY_FIELD_POSITION_SYMBOL:
                self.update_hero_position_in_map_as_list(hero_current_column, hero_current_row,
                                                         hero_new_column, hero_new_row)
                self.hero.take_mana(self.hero.mana_regeneration_rate)
        except IndexError:
            pass
