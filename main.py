from main.constants import (INTRO_TEXT, CREATE_HERO_TEXT, HERO_HEALTH_WHEN_INITIALISING,
                            HERO_MANA_WHEN_INITIALISING, HERO_MANA_REGENERATION_RATE_WHEN_INITIALISING,
                            DEFAULT_WEAPON_NAME, DEFAULT_WEAPON_DAMAGE, HERO_INFORMATION_TEXT)
from main.utils import new_screen, wait_for_continue_command
from main.models.hero import Hero
from main.treasures.weapon import Weapon


def print_intro():
    new_screen()
    print(INTRO_TEXT)


def execute_intro():
    print_intro()
    wait_for_continue_command()


def read_name_and_title_for_hero():
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
    name, title = read_name_and_title_for_hero()
    hero = Hero(name=name, title=title, health=HERO_HEALTH_WHEN_INITIALISING,
                mana=HERO_MANA_WHEN_INITIALISING, mana_regeneration_rate=HERO_MANA_REGENERATION_RATE_WHEN_INITIALISING)
    hero = equip_hero_with_default_weapon(hero)
    wait_for_continue_command()
    return hero


def main():
    execute_intro()
    hero = create_hero()
    print_hero_initial_information(hero)


if __name__ == '__main__':
    main()
