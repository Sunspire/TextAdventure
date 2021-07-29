import functions.globals
import colorama
from termcolor import colored
from classes.player import Player
from classes.action import actions

colorama.init()
functions.globals.init()

is_exit = False
the_player = Player('Solargazer', 'An adventurer', 100)
the_world = functions.globals.the_world
current_tile = the_world.tiles[(the_player.x, the_player.y)]

def evaluate_command(the_input):
    the_input = the_input.strip().lower()

    if not the_input:
        return

    if the_input == 'q':
        confirm_exit = input(colored('are you sure (y/n)? > ', 'yellow'))

        if confirm_exit.strip().lower() == 'y':
            return True

        print(colored('Returning to game.', 'green'))
        return False

    first_word_in_command = the_input.split()[0]

    for action in actions:
        if action.command == first_word_in_command:
            the_player.command = the_input
            the_player.do_action(action)
            break
    else:
        print(colored('Unknown command', 'red'))

    return False


# testing
the_world.test_override()

while not is_exit:
    command = input(colored(f'{the_player} > ', 'cyan'))
    is_exit = evaluate_command(command)
