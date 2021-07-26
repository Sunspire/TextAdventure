from functions.general import *
from classes.player import Player
from classes.world import World
from classes.action import actions

is_exit = False

the_player = Player('Solargazer', 'An adventurer', 100)

the_world = World()
the_world.load_tiles()


def evaluate_command(the_input):
    the_input = the_input.strip().lower()

    if not the_input:
        return

    if the_input == 'exit':
        confirm_exit = input(output('are you sure (y/n)? > ', 'yellow'))

        if confirm_exit.strip().lower() == 'y':
            print(output('', 'reset'))
            return True

        print(output('Returning to game.', 'green'))
        return False

    first_word_in_command = the_input.split()[0]

    for action in actions:
        if action.command == first_word_in_command:
            the_player.command = the_input
            the_player.do_action(action, the_world)
            break
    else:
        print(output('Unknown command', 'red'))

    return False


# testing
the_world.test_override()

while not is_exit:
    command = input(output('{} > '.format(the_player), 'cyan'))
    is_exit = evaluate_command(command)
