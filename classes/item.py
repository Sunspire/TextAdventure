from dataclasses import dataclass


@dataclass
class Item:
    name: str
    value: int
    description: str = ''


class Weapon(Item):
    def __init__(self, name, description, value):
        super().__init__(name, value, description)
