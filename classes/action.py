from classes.player import Player


class action:
    def __init__(self, method, name, command):
        self.method = method
        self.name = name
        self.command = command


def action_list():
    act_list = []
    act_list.append(
        action(method=Player.move_north, name='Move north', command='w'))
    act_list.append(
        action(method=Player.move_south, name='Move south', command='s'))
    act_list.append(
        action(method=Player.move_east, name='Move east', command='d'))
    act_list.append(
        action(method=Player.move_west, name='Move west', command='a'))
    act_list.append(action(method=Player.look, name='Look', command='look'))
    act_list.append(action(method=Player.examine_item, name='Examine item',
                           command='examine'))
    act_list.append(
        action(method=Player.examine_item, name='Examine item', command='exam'))
    return act_list
