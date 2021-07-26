from dataclasses import dataclass


class MapTile(dataclass):

    x: int
    y: int
    description: str = ''


class Tile(MapTile):

    def __init__(self, x, y, description='', items=None):
        super().__init__(x, y, description)

        if items is None:
            items = []

        self.items = items
