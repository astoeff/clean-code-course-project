import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from utils import validate_dungeon_map


class Dungeon:
    def __init__(self, file):
        self.map = self.map_file_to_string(file)
        self.checkpoints = 0

    @property
    def map(self):
        return self.map

    @map.setter
    def map(self, m):
        validate_dungeon_map(m)
        self.map = m

    def map_file_to_string(self, file):
        with open(file, 'r') as f:
            return f.read()
