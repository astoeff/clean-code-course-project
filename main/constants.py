PLAYER_MAX_MANA_AND_HEALTH_VALUE = 100
PLAYER_MIN_MANA_AND_HEALTH_VALUE = 0
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

LEGEND = '\nLEGEND:'\
         'S - spawning position           ' + 'C - checkpoint'\
         'G - exit of the dungeon         ' + 'T - treasure'\
         '# - obstacle                    ' + 'E - enemy\n'

STOP_RESULT = 'stop'
PLAYER_AVAILABLE_COMMANDS_TEXT = 'Press w,s,a, d to move or x to attack from distance by spell ...\n'
PLAYER_AVAILABLE_COMMANDS_LIST_OF_SYMBOLS = ['w', 's', 'a', 'd', 'x']

ATTACK_KEY = 'x'
MOVEMENT_DIRECTION_BY_SYMBOL_DICTIONARY = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
GATE_FIELD = 'G'
CONGRATULATIONS_TEXT = 'Congratulations, you have won!\n' + 100 * '*'
ACHIEVED_TREASURE_TEXT = 'You just received:\n'

DUNGEON_MAP_STARTING_POSITION_SYMBOL = 'S'
ERROR_MESSAGE_IF_NO_STARTING_POSITION_IN_DUNGEON_MAP = 'No starting point'
DUNGEON_MAP_GATE_POSITION_SYMBOL = 'G'