import subprocess

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from constants import CLEAR_BASH_COMMAND,C_KEY, MESSAGE_FOR_CONTINUE
from read_input_help_library import get_character


def new_screen():
    subprocess.call(CLEAR_BASH_COMMAND)


def check_if_correct_key_is_pressed(symbols, pressed):
    is_correct_key_pressed = False
    for symbol in symbols:
        if pressed == symbol:
            is_correct_key_pressed = True
            break
    return is_correct_key_pressed


def wait_until_symbol_from_list_of_symbols_is_read_from_console(symbols, message):
    print(message)
    pressed = None
    is_correct_key_pressed = False
    while not is_correct_key_pressed:
        pressed = str(get_character())[2]
        pressed = pressed.lower()
        is_correct_key_pressed = check_if_correct_key_is_pressed(symbols, pressed)


def wait_for_continue_command():
    symbol = C_KEY
    message = MESSAGE_FOR_CONTINUE
    wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)


def show_message_screen(message):
    new_screen()
    print(message)
    print()
    wait_for_continue_command()


def validate_dungeon_map(dungeon_map):
    assert 'S' in dungeon_map, "No starting point"

    gates = 0
    for symbol in dungeon_map:
        if symbol == "G":
            gates += 1
    assert gates == 1, "Number of gates != 1"