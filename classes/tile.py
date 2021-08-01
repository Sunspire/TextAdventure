from dataclasses import dataclass
from classes.item import Item, Weapon, Armor
from classes.npc import Npc


@dataclass
class Tile:
    description: str = ''
    __items = []
    __npcs = []

    def set_item(self, item):
        if isinstance(item, Item) or isinstance(item, Weapon) or isinstance(item, Armor):
            self.__items.append(item)
        else:
            raise TypeError("Only objects of type 'Item', 'Weapon' or 'Armor' are allowed")

    def get_items(self):
        return self.__items

    def set_npc(self, npc: Npc):
        if isinstance(npc, Npc):
            self.__npcs.append(npc)
        else:
            raise TypeError("Only object of type 'Npc' is allowed")

    def get_npcs(self):
        return self.__npcs