class Treasure:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def set_for_player(self, player):
        pass

    def __str__(self):
        pass
