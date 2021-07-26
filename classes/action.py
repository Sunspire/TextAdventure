from classes.item import item
from classes.player import player

class action():
    def __init__(self, method,  name, command):
        self.method = method
        self.name = name
        self.command = command

def action_list():
    act_list = []
    act_list.append(action(method=player.move_north, name='Move north', command='w'))
    act_list.append(action(method=player.move_south, name='Move south', command='s'))
    act_list.append(action(method=player.move_east, name='Move east', command='d'))
    act_list.append(action(method=player.move_west, name='Move west', command='a'))
    return act_list