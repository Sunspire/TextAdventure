from enum import Enum


class ItemType(Enum):
    armor = 'armor'
    clutter = 'clutter'
    weapon = 'weapon'

class ArmorSlot(Enum):
    head = 'head'
    torso = 'torso'
    arms = 'arms'
    legs = 'legs'
    feet = 'feet'
    shield = 'shield'

class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.value: int = 0
        self.item_type: str = ItemType.clutter

class Weapon(Item):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.item_type: str = ItemType.weapon
        self.damage: int = 0

class Armor(Item):
    def __init__(self, name: str, description: str, armor_slot: str):
        self.name = name
        self.description = description
        self.armor_slot = armor_slot
        self.item_type: str = ItemType.armor
        self.protection: int = 0