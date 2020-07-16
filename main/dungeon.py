import sys
from copy import deepcopy
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from utils import validate_dungeon_map, check_is_row_or_column_inside_map
from constants import (DUNGEON_MAP_STARTING_POSITION_SYMBOL, DUNGEON_MAP_HERO_POSITION_SYMBOL,
                       DUNGEON_MAP_ROW_SEPARATOR, UP_DIRECTION_STRING, DOWN_DIRECTION_STRING,
                       LEFT_DIRECTION_STRING, RIGHT_DIRECTION_STRING, DUNGEON_MAP_EMPTY_FIELD_POSITION_SYMBOL,
                       DUNGEON_MAP_TREASURE_POSITION_SYMBOL, DUNGEON_MAP_ENEMY_POSITION_SYMBOL,
                       DUNGEON_MAP_CHECKPOINT_POSITION_SYMBOL, DUNGEON_MAP_GATE_POSITION_SYMBOL,
                       ACHIEVED_TREASURE_RESULT_FROM_MOVEMENT, REACHED_ENEMY_RESULT_FROM_MOVEMENT,
                       REACHED_CHECKPOINT_RESULT_FROM_MOVEMENT, REACHED_GATE_RESULT_FROM_MOVEMENT,
                       DUNGEON_INITIAL_CHECKPOINTS_COUNT, FILE_OPEN_IN_READING_MODE)


class Dungeon:
    def __init__(self, file):
        self.map = self.map_file_to_string(file)
        self.hero = None
        self.checkpoints = DUNGEON_INITIAL_CHECKPOINTS_COUNT

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
        self.map = self.convert_map_as_list_to_string(m)
        self._map_as_list = deepcopy(m)

    def map_file_to_string(self, file):
        with open(file, FILE_OPEN_IN_READING_MODE) as f:
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

        result_from_movement = None
        if check_is_row_or_column_inside_map(hero_new_row, hero_new_column):
            try:
                if self.map_as_list[hero_new_row][hero_new_column] == DUNGEON_MAP_EMPTY_FIELD_POSITION_SYMBOL:
                    self.update_hero_position_in_map_as_list(hero_current_column, hero_current_row,
                                                             hero_new_column, hero_new_row)
                    self.hero.take_mana(self.hero.mana_regeneration_rate)
                elif self.map_as_list[hero_new_row][hero_new_column] == DUNGEON_MAP_TREASURE_POSITION_SYMBOL:
                    self.update_hero_position_in_map_as_list(hero_current_column, hero_current_row,
                                                             hero_new_column, hero_new_row)
                    result_from_movement = ACHIEVED_TREASURE_RESULT_FROM_MOVEMENT
                elif self.map_as_list[hero_new_row][hero_new_column] == DUNGEON_MAP_ENEMY_POSITION_SYMBOL:
                    self.update_hero_position_in_map_as_list(hero_current_column, hero_current_row,
                                                             hero_new_column, hero_new_row)
                    result_from_movement = REACHED_ENEMY_RESULT_FROM_MOVEMENT
                elif self.map_as_list[hero_new_row][hero_new_column] == DUNGEON_MAP_CHECKPOINT_POSITION_SYMBOL:
                    self.update_hero_position_in_map_as_list(hero_current_column, hero_current_row,
                                                             hero_new_column, hero_new_row)
                    result_from_movement = REACHED_CHECKPOINT_RESULT_FROM_MOVEMENT
                elif self.map_as_list[hero_new_row][hero_new_column] == DUNGEON_MAP_GATE_POSITION_SYMBOL:
                    self.update_hero_position_in_map_as_list(hero_current_column, hero_current_row,
                                                             hero_new_column, hero_new_row)
                    result_from_movement = REACHED_GATE_RESULT_FROM_MOVEMENT
            except IndexError:
                pass
        return result_from_movement
