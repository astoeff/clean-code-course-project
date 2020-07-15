from main.constants import (INTRO_TEXT, CREATE_HERO_TEXT, HERO_HEALTH_WHEN_INITIALISING,
                            HERO_MANA_WHEN_INITIALISING, HERO_MANA_REGENERATION_RATE_WHEN_INITIALISING,
                            DEFAULT_WEAPON_NAME, DEFAULT_WEAPON_DAMAGE, HERO_INFORMATION_TEXT, STOP_RESULT,
                            PLAYER_AVAILABLE_COMMANDS_TEXT, PLAYER_AVAILABLE_COMMANDS_LIST_OF_KEYS, LEGEND,
                            ATTACK_KEY, MOVEMENT_DIRECTION_BY_SYMBOL_DICTIONARY, DUNGEON_MAP_GATE_POSITION_SYMBOL,
                            CONGRATULATIONS_TEXT, ACHIEVED_TREASURE_TEXT, LEVEL_1_MAP_FILE, QUIT_KEY,
                            ACHIEVED_TREASURE_RESULT_FROM_MOVEMENT, REACHED_ENEMY_RESULT_FROM_MOVEMENT,
                            REACHED_CHECKPOINT_RESULT_FROM_MOVEMENT, REACHED_GATE_RESULT_FROM_MOVEMENT,
                            INPUT_NAME_TEXT, INPUT_TITLE_TEXT, GAME_OVER_TEXT)
from main.utils import (new_screen, wait_for_continue_command, wait_until_key_from_list_of_keys_is_pressed,
                        show_message_screen, generate_random_treasure_from_file)
from main.models.hero import Hero
from main.treasures.weapon import Weapon
from main.treasures.treasure import Treasure
from main.dungeon import Dungeon
import time


def print_intro():
    new_screen()
    print(INTRO_TEXT)


def execute_intro():
    print_intro()
    wait_for_continue_command()


def read_input_name_and_title_for_hero():
    new_screen()
    print(CREATE_HERO_TEXT)
    name = input(INPUT_NAME_TEXT)
    title = input(INPUT_TITLE_TEXT)
    return (name, title)


def equip_hero_with_default_weapon(hero):
    default_weapon = Weapon(name=DEFAULT_WEAPON_NAME, damage=DEFAULT_WEAPON_DAMAGE)
    hero.equip(default_weapon)
    return hero


def print_hero_initial_information(hero):
    new_screen()
    print(HERO_INFORMATION_TEXT)
    hero.print_hero()
    wait_for_continue_command()


def create_hero():
    name, title = read_input_name_and_title_for_hero()
    hero = Hero(name=name, title=title, health=HERO_HEALTH_WHEN_INITIALISING,
                mana=HERO_MANA_WHEN_INITIALISING, mana_regeneration_rate=HERO_MANA_REGENERATION_RATE_WHEN_INITIALISING)
    hero = equip_hero_with_default_weapon(hero)
    wait_for_continue_command()
    return hero


def print_map_with_legend(dungeon):
    print(dungeon.map)
    print(LEGEND)


def get_pressed_key_for_turn():
    keys = PLAYER_AVAILABLE_COMMANDS_LIST_OF_KEYS
    message = PLAYER_AVAILABLE_COMMANDS_TEXT
    pressed_key = wait_until_key_from_list_of_keys_is_pressed(keys, message)
    return pressed_key


def show_achieved_treasure(treasure):
    new_screen()
    print(treasure)
    wait_for_continue_command()


def select_screen_depending_on_result_from_movement(result_from_movement):
    is_treasure_achieved_after_movement = result_from_movement == ACHIEVED_TREASURE_RESULT_FROM_MOVEMENT
    is_gate_reached_after_movement = result_from_movement == REACHED_GATE_RESULT_FROM_MOVEMENT
    is_enemy_reached_after_movement = result_from_movement == REACHED_ENEMY_RESULT_FROM_MOVEMENT
    is_checkpoint_reached_after_movement = result_from_movement == REACHED_CHECKPOINT_RESULT_FROM_MOVEMENT
    if is_treasure_achieved_after_movement:
        treasure = generate_random_treasure_from_file()
        show_achieved_treasure(treasure)
    elif is_gate_reached_after_movement:
        raise SystemExit()
    elif is_enemy_reached_after_movement:
        pass
    elif is_checkpoint_reached_after_movement:
        pass


def move_hero(dungeon, pressed_key_for_turn):
    movement_direction = MOVEMENT_DIRECTION_BY_SYMBOL_DICTIONARY[pressed_key_for_turn]
    result_from_movement = dungeon.move_hero(movement_direction)
    select_screen_depending_on_result_from_movement(result_from_movement)


def select_player_turn_depending_on_pressed_key_for_turn(dungeon, pressed_key_for_turn):
    is_attack_key_pressed = pressed_key_for_turn == ATTACK_KEY
    is_quit_key_pressed = pressed_key_for_turn == QUIT_KEY
    if is_attack_key_pressed:
        pass
    elif is_quit_key_pressed:
        raise SystemExit()
    else:
        move_hero(dungeon, pressed_key_for_turn)


def game_turn(dungeon):
    new_screen()
    print_map_with_legend(dungeon)
    pressed_key_for_turn = get_pressed_key_for_turn()
    select_player_turn_depending_on_pressed_key_for_turn(dungeon, pressed_key_for_turn)


def show_game_over_screen():
    new_screen()
    print(GAME_OVER_TEXT)


def play_game(hero, dungeon):
    dungeon.spawn(hero)
    is_game_in_process = True
    while is_game_in_process:
        try:
            game_turn(dungeon)
            if not dungeon.hero.is_alive():
                is_game_in_process = False
        except SystemExit:
            is_game_in_process = False
    show_game_over_screen()


def main():
    execute_intro()
    hero = create_hero()
    print_hero_initial_information(hero)
    dungeon = Dungeon(LEVEL_1_MAP_FILE)
    play_game(hero, dungeon)


if __name__ == '__main__':
    main()
