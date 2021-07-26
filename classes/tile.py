import classes.item


class MapTile:
    def __init__(self, x, y, description=''):
        self.x = x
        self.y = y
        self.description = description


class Tile(MapTile):
    def __init__(self, x, y, description='', items=[]):
        self.items = items
        super().__init__(x, y, description)
