from collections import Callable
from dataclasses import dataclass

from classes.player import Player


@dataclass
class Action:
    method: Callable
    name: str
    command: str


actions = [
    Action(Player.move_north, 'Move north', 'w')
    ,Action(Player.move_south, 'Move south', 's')
    ,Action(Player.move_east, 'Move east', 'd')
    ,Action(Player.move_west, 'Move west', 'a')
    ,Action(Player.look, 'Look', 'look')
    ,Action(Player.examine_item, 'Examine item', 'examine')
    ,Action(Player.examine_item, 'Examine item', 'exam')
    ,Action(Player.take_item, 'Take item', 'take')
    ,Action(Player.look_inventory, 'Inventory', 'i')
    ,Action(Player.drop_inventory_item, 'Drop item', 'drop')
    ,Action(Player.attack_npc, 'Attack', 'attack')
    ,Action(Player.attack_npc, 'Attack', 'kill')
]
