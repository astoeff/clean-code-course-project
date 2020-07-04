from main.constants import (INTRO_TEXT, CREATE_HERO_TEXT, HERO_HEALTH_WHEN_INITIALISING,
                            HERO_MANA_WHEN_INITIALISING, HERO_MANA_REGENERATION_RATE_WHEN_INITIALISING,
                            DEFAULT_WEAPON_NAME, DEFAULT_WEAPON_DAMAGE, HERO_INFORMATION_TEXT, STOP_RESULT,
                            PLAYER_AVAILABLE_COMMANDS_TEXT, PLAYER_AVAILABLE_COMMANDS_LIST_OF_SYMBOLS, LEGEND,
                            ATTACK_KEY, MOVEMENT_DIRECTION_BY_SYMBOL_DICTIONARY, GATE_FIELD, CONGRATULATIONS_TEXT,
                            ACHIEVED_TREASURE_TEXT)
from main.utils import (new_screen, wait_for_continue_command,
                        wait_until_symbol_from_list_of_symbols_is_read_from_console, show_message_screen)
from main.models.hero import Hero
from main.treasures.weapon import Weapon
from main.treasures.treasure import Treasure
from main.dungeon import Dungeon


def print_intro():
    new_screen()
    print(INTRO_TEXT)


def execute_intro():
    print_intro()
    wait_for_continue_command()


def read_input_name_and_title_for_hero():
    new_screen()
    print(CREATE_HERO_TEXT)
    name = input('Name: ')
    title = input('Title: ')
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


def select_move_key():
    symbols = PLAYER_AVAILABLE_COMMANDS_LIST_OF_SYMBOLS
    message = PLAYER_AVAILABLE_COMMANDS_TEXT
    pressed_key = wait_until_symbol_from_list_of_symbols_is_read_from_console(symbols, message)
    return pressed_key


def select_screen_depending_on_result_from_movement(result_from_movement):
    is_treasure_achieved_after_movement = isinstance(result_from_movement, Treasure)
    is_hero_in_enemy_field_after_movement = True
    if result_from_movement == GATE_FIELD:
        show_message_screen(CONGRATULATIONS_TEXT)
        return STOP_RESULT
    elif is_treasure_achieved_after_movement:
        show_message_screen(ACHIEVED_TREASURE_TEXT + str(result_from_movement))
    elif is_hero_in_enemy_field_after_movement:
        show_automatic_attack_screen(result_from_movement)


def process_hero_movement(dungeon, pressed_key):
    movement_direction = MOVEMENT_DIRECTION_BY_SYMBOL_DICTIONARY[pressed_key]
    result_from_movement = dungeon.move_hero(movement_direction)
    select_screen_depending_on_result_from_movement(result_from_movement)


def select_screen_depending_on_pressed_key(hero, dungeon, pressed_key):
    is_attack_key_pressed = pressed_key == ATTACK_KEY
    if is_attack_key_pressed:
        show_attack_screen(dungeon)
    else:
        process_hero_movement(dungeon)


def show_move_screen(hero, dungeon):
    new_screen()
    print_map_with_legend(dungeon)
    move_key = select_move_key()




def show_game_over_screen():
    pass


def play_game(hero, dungeon):
    dungeon.spawn(hero)
    is_game_in_process = True
    while is_game_in_process:
        result = show_move_screen(hero, dungeon)
        if not dungeon.hero.is_alive():
            is_game_in_process = False
        else:
            if result == STOP_RESULT:
                is_game_in_process = False
    show_game_over_screen()

def main():
    execute_intro()
    hero = create_hero()
    print_hero_initial_information(hero)
    dungeon = Dungeon()
    play_game(hero, dungeon)


if __name__ == '__main__':
    main()
