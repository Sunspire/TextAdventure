from collections import Callable
from dataclasses import dataclass

from classes.player import Player


@dataclass
class Action:
    method: Callable
    name: str
    command: str


actions = [
    Action(Player.move_north, 'Move north', 'w'),
    Action(Player.move_south, 'Move south', 's'),
    Action(Player.move_east, 'Move east', 'd'),
    Action(Player.move_west, 'Move west', 'a'),
    Action(Player.look, 'Look', 'look'),
    Action(Player.examine_item, 'Examine item', 'examine'),
    Action(Player.examine_item, 'Examine item', 'exam')
]
