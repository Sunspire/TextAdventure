from classes.player import Player


class Action:

    def __init__(self, method, name, command):
        self.method = method
        self.name = name
        self.command = command


def action_list():
    return [
        Action(method=Player.move_north, name='Move north', command='w'),
        Action(method=Player.move_south, name='Move south', command='s'),
        Action(method=Player.move_east, name='Move east', command='d'),
        Action(method=Player.move_west, name='Move west', command='a'),
        Action(method=Player.look, name='Look', command='look'),
        Action(
            method=Player.examine_item, name='Examine item', command='examine'
        ),
        Action(method=Player.examine_item, name='Examine item', command='exam')
    ]
