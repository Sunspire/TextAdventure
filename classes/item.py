from dataclasses import dataclass


@dataclass
class Item:
    name: str
    description: str = ''
    value: int = 0


class Weapon(Item):
    def __init__(self, name, description, value):
        super().__init__(name, value, description)
