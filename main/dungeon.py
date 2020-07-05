import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from utils import validate_dungeon_map
from constants import DUNGEON_MAP_STARTING_POSITION_SYMBOL, DUNGEON_MAP_HERO_POSITION_SYMBOL


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
