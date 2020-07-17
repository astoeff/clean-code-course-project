import subprocess

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from constants import (CLEAR_BASH_COMMAND, C_KEY, MESSAGE_FOR_CONTINUE, TREASURES_FILE, FILE_READING_MODE,
                       TREASURE_ARGUMENTS_SEPARATOR_IN_TREASURES_FILE, SPELL_CLASS_IN_TREASURES_FILE_STRING,
                       WEAPON_CLASS_IN_TREASURES_FILE_STRING, HEALTH_POTION_CLASS_IN_TREASURES_FILE_STRING,
                       MANA_POTION_IN_TREASURES_FILE_STRING, DUNGEON_MAP_STARTING_POSITION_SYMBOL,
                       DUNGEON_MAP_GATE_POSITION_SYMBOL, DUNGEON_GATES_NUMBER,
                       VALIDATE_DUNGEON_NO_STARTING_POSITION_ERROR_TEXT,
                       VALIDATE_DUNGEON_NUMBER_OF_GATES_NOT_ONE_ERROR_TEXT, DUNGEON_MAP_FIRST_ROW_AND_COLUMN_NUMBER)
from read_input_help_library import get_character
from treasures.spell import Spell
from treasures.weapon import Weapon
from treasures.health_potion import HealthPotion
from treasures.mana_potion import ManaPotion
import random


def new_screen():
    subprocess.call(CLEAR_BASH_COMMAND)


def check_if_correct_key_is_pressed(symbols, pressed):
    is_correct_key_pressed = pressed in symbols
    return is_correct_key_pressed


def wait_until_key_from_list_of_keys_is_pressed(symbols, message):
    print(message)
    pressed_key = None
    is_correct_key_pressed = False
    while not is_correct_key_pressed:
        pressed_key = str(get_character())[2]
        pressed_key = pressed_key.lower()
        is_correct_key_pressed = check_if_correct_key_is_pressed(symbols, pressed_key)
    return pressed_key


def wait_for_continue_command():
    keys = [C_KEY]
    message = MESSAGE_FOR_CONTINUE
    wait_until_key_from_list_of_keys_is_pressed(keys, message)


def show_message_screen(message):
    new_screen()
    print(message)
    print()
    wait_for_continue_command()


def validate_dungeon_map(dungeon_map):
    assert DUNGEON_MAP_STARTING_POSITION_SYMBOL in dungeon_map, VALIDATE_DUNGEON_NO_STARTING_POSITION_ERROR_TEXT

    gates_count = 0
    for symbol in dungeon_map:
        if symbol == DUNGEON_MAP_GATE_POSITION_SYMBOL:
            gates_count += 1
    assert gates_count == DUNGEON_GATES_NUMBER, VALIDATE_DUNGEON_NUMBER_OF_GATES_NOT_ONE_ERROR_TEXT


def check_is_row_and_column_inside_map(row, column):
    is_row_inside_map = row >= DUNGEON_MAP_FIRST_ROW_AND_COLUMN_NUMBER
    is_column_inside_map = column >= DUNGEON_MAP_FIRST_ROW_AND_COLUMN_NUMBER
    return is_row_inside_map and is_column_inside_map


def create_treasure_instance_by_list_of_args(treasure_args_list):
    treasure_first_arg = treasure_args_list[0]
    if treasure_first_arg == SPELL_CLASS_IN_TREASURES_FILE_STRING:
        treasure = Spell(name=treasure_args_list[1], damage=int(treasure_args_list[2]),
                         mana_cost=int(treasure_args_list[3]), cast_range=int(treasure_args_list[4]))
    elif treasure_first_arg == WEAPON_CLASS_IN_TREASURES_FILE_STRING:
        treasure = Weapon(name=treasure_args_list[1], damage=int(treasure_args_list[2]))
    elif treasure_first_arg == HEALTH_POTION_CLASS_IN_TREASURES_FILE_STRING:
        treasure = HealthPotion(name=treasure_args_list[1], healing=treasure_args_list[2])
    elif treasure_first_arg == MANA_POTION_IN_TREASURES_FILE_STRING:
        treasure = ManaPotion(name=treasure_args_list[1], mana_regeneration=treasure_args_list[2])
    return treasure


def generate_random_treasure_from_file():
    with open(TREASURES_FILE, FILE_READING_MODE) as f:
        treasures_in_file = f.read().splitlines()
        treasure_args_string = random.choice(treasures_in_file)
        treasure_args_list = treasure_args_string.split(TREASURE_ARGUMENTS_SEPARATOR_IN_TREASURES_FILE)
        treasure = create_treasure_instance_by_list_of_args(treasure_args_list)
        return treasure
