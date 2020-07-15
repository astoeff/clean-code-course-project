PLAYER_MAX_MANA_AND_HEALTH_VALUE = 100
PLAYER_MIN_MANA_AND_HEALTH_VALUE = 0
PLAYER_ZERO_DAMAGE_WHEN_ATTACKING = 0
PLAYER_ATTACK_BY_WEAPON_STRING = 'weapon'
PLAYER_ATTACK_BY_SPELL_STRING = 'spell'
ENEMY_MIN_MANA_AND_HEALTH_WHEN_INITIALISING = 50
ENEMY_MAX_MANA_AND_HEALTH_WHEN_INITIALISING = 100
ENEMY_MIN_DAMAGE_WHEN_INITIALISING = 10
ENEMY_MAX_DAMAGE_WHEN_INITIALISING = 50
INVALID_WEAPON_VALUE_ERROR_TEXT = 'Invalid weapon given for equipment'
INVALID_SPELL_VALUE_ERROR_TEXT = 'Invalid spell given for learning'

INTRO_TEXT = 'Hi, a game has just started!\n\n'\
             'You are put in a magic dungeon with TREASURES (T) '\
             'and your task is to make through the exit (G), but be carefull!\n'\
             'There are ENEMIES (E) that you need to fight and obstacles (#).\n'\
             'You can attack your enemies from a distance by spell but only if the range of the spell allows it.\n'\
             'To make it easier for you, there are checkpoints (C) in the dungeon.\n'\
             'Your hero respawns on the latest checkpoint.\n'\
             'If you are dead and have not go through any checkpoints this life, you lose the game!\n'\
             'Good luck!\n'

CLEAR_BASH_COMMAND = 'clear'
C_KEY = 'c'
MESSAGE_FOR_CONTINUE = 'Press c for continue ...'

CREATE_HERO_TEXT = 'Now enter name and title for your hero\n'\
                   'Example: Bron, Dragonslayer\n'

HERO_HEALTH_WHEN_INITIALISING = 100
HERO_MANA_WHEN_INITIALISING = 100
HERO_MANA_REGENERATION_RATE_WHEN_INITIALISING = 2

DEFAULT_WEAPON_NAME = 'knife'
DEFAULT_WEAPON_DAMAGE = 10
HERO_INFORMATION_TEXT = 'Information for hero:\n'

LEGEND = '\nLEGEND:\n'\
         'S - spawning position           ' + 'C - checkpoint\n'\
         'G - exit of the dungeon         ' + 'T - treasure\n'\
         '# - obstacle                    ' + 'E - enemy\n'

STOP_RESULT = 'stop'
PLAYER_AVAILABLE_COMMANDS_TEXT = 'Press w, s, a, d to move or x to attack from distance by spell ...\n      q for quit'
PLAYER_AVAILABLE_COMMANDS_LIST_OF_KEYS = ['w', 's', 'a', 'd', 'x', 'q']

ATTACK_KEY = 'x'
QUIT_KEY = 'q'
MOVEMENT_DIRECTION_BY_SYMBOL_DICTIONARY = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}

CONGRATULATIONS_TEXT = 'Congratulations, you have won!\n' + 100 * '*'
ACHIEVED_TREASURE_TEXT = 'You just received:\n'

DUNGEON_MAP_STARTING_POSITION_SYMBOL = 'S'
ERROR_MESSAGE_IF_NO_STARTING_POSITION_IN_DUNGEON_MAP = 'No starting point'
DUNGEON_MAP_GATE_POSITION_SYMBOL = 'G'
ERROR_MESSAGE_IF_INVALID_NUMBER_OF_GATES_IN_DUNGEON_MAP = 'Number of gates != 1'
DUNGEON_MAP_HERO_POSITION_SYMBOL = 'H'
STOP_RESULT = 'stop'
LEVEL_1_MAP_FILE = 'main/maps/level1.txt'
DUNGEON_MAP_ROW_SEPARATOR = '\n'

UP_DIRECTION_STRING = 'up'
DOWN_DIRECTION_STRING = 'down'
LEFT_DIRECTION_STRING = 'left'
RIGHT_DIRECTION_STRING = 'right'
DIRECTIONS_WITH_THEIR_OPPOSITES_DICTIONARY = {UP_DIRECTION_STRING: DOWN_DIRECTION_STRING,
                                              DOWN_DIRECTION_STRING: UP_DIRECTION_STRING,
                                              LEFT_DIRECTION_STRING: RIGHT_DIRECTION_STRING,
                                              RIGHT_DIRECTION_STRING: LEFT_DIRECTION_STRING}
DUNGEON_MAP_EMPTY_FIELD_POSITION_SYMBOL = '.'
DUNGEON_MAP_TREASURE_POSITION_SYMBOL = 'T'
DUNGEON_MAP_ENEMY_POSITION_SYMBOL = 'E'
DUNGEON_MAP_CHECKPOINT_POSITION_SYMBOL = 'C'
DUNGEON_MAP_GATE_POSITION_SYMBOL = 'G'

ACHIEVED_TREASURE_RESULT_FROM_MOVEMENT = 'treasure'
REACHED_GATE_RESULT_FROM_MOVEMENT = 'gate'
REACHED_ENEMY_RESULT_FROM_MOVEMENT = 'enemy'
REACHED_CHECKPOINT_RESULT_FROM_MOVEMENT = 'checkpoint'
TREASURES_FILE = 'main/treasures/treasures.txt'
FILE_READING_MODE = 'r'
TREASURE_ARGUMENTS_SEPARATOR_IN_TREASURES_FILE = ','
SPELL_CLASS_IN_TREASURES_FILE_STRING = 'Spell'
WEAPON_CLASS_IN_TREASURES_FILE_STRING = 'Weapon'
HEALTH_POTION_CLASS_IN_TREASURES_FILE_STRING = 'HealthPotion'
MANA_POTION_IN_TREASURES_FILE_STRING = 'ManaPotion'
INPUT_NAME_TEXT = 'Name: '
INPUT_TITLE_TEXT = 'Title: '
GAME_OVER_TEXT = 'Bye bye!'

FIGHT_INITIAL_INFORMATION_PART = 'A fight started between your hero and '
FIGHT_HERO_ATTACK_INFORMATION_PART = 'Hero attacks for '
FIGHT_ENEMY_ATTACK_INFORMATION_PART = 'Enemy attacks for '
FIGHT_HERO_CANNOT_ATTACK_INFORMATION_PART = 'Hero cannot attack!'
FIGHT_ENEMY_CANNOT_ATTACK_INFORMATION_PART = 'Enemy cannot attack!'
