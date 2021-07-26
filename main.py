from functions.general import *
from classes.player import Player
from classes.world import World
from classes.action import action_list

is_exit = 0
the_player = Player('Solargazer', 'An adventurer', 100)
the_player.x = 0
the_player.y = 0
the_world = World()
the_world.load_tiles()
actions = action_list()


def evaluate_command(the_input):
    the_input = the_input.strip().lower()
    if the_input != '':
        command_not_found = True

        if the_input == 'exit':
            confirm_exit = input(output('are you sure (y/n)? > ', 'yellow'))
            if confirm_exit.strip().lower() == 'y':
                global is_exit
                is_exit = 1
                print(output('', 'reset'))
            else:
                print(output('Returning to game.', 'green'))
        else:
            first_word_in_command = the_input.split()[0]
            for i in range(len(actions)):
                if first_word_in_command == actions[i].command:
                    the_player.command = the_input
                    the_player.do_action(actions[i], the_world)
                    command_not_found = False
                    break

            if command_not_found:
                print(output('Unknown command', 'red'))


# testing
the_world.test_override()

while is_exit == 0:
    # print(output("({},{})".format(the_player.x, the_player.y), 'green'))
    command = input(output('{} > '.format(the_player), 'cyan'))
    evaluate_command(command)
