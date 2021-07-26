from functions.general import *
from classes.player import player
from classes.world import world
from classes.action import action_list

is_exit = 0
the_player = player('Solargazer', 'An adventurer', 100)
the_player.x = 0
the_player.y = 0
the_world = world()
the_world.load_tiles()
actions = action_list()

def evaluate_command(the_input):
    the_input = the_input.strip().lower()
    if the_input != '':
        global the_player
        command_not_found = True
        
        if the_input == 'exit':
            confirm_exit = input(output('are you sure (y/n)? > '.format(the_player), 'yellow'))
            if confirm_exit.strip().lower() == 'y':
                global is_exit
                is_exit = 1
        else:
            for i in range(len(actions)):
                if the_input == actions[i].command:
                    the_player.do_action(actions[i], the_world)
                    command_not_found = False
                    break

            if (command_not_found):
                print(output('Unknown command', 'red'))
                
while is_exit == 0:    
    print(output("({},{})".format(the_player.x, the_player.y), 'green'))
    command = input(output('{} > '.format(the_player), 'cyans'))
    evaluate_command(command)

'''
        if input == 'w': new_y = y - 1
        if input == 's': new_y = y + 1
        if input == 'a': new_x = x - 1
        if input == 'd': new_x = x + 1
        new_position = (new_x, new_y)
        
        if world.get(new_position):
            x = new_x
            y = new_y
            position = new_position
            print(world.get(position))
        else:
            print('you cannot move there')
'''