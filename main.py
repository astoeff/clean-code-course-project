from main.constants import INTRO_TEXT
from main.utils import new_screen, wait_for_continue_command


def print_intro():
    new_screen()
    print(INTRO_TEXT)


def execute_intro():
    print_intro()
    wait_for_continue_command()


def main():
    execute_intro()


if __name__ == '__main__':
    main()
