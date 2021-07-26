from functions.general import output


class Player:
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp
        self.x = 0
        self.y = 0
        self.command = ''

    def __str__(self):
        return "{}, {}".format(self.name, self.hp)

    def move(self, lx, ly, the_world, direction):
        if the_world.tile_exists((self.x + lx, self.y + ly)):
            self.x += lx
            self.y += ly

            print(output('You move {}.'.format(direction), 'green'))
            print('')
            self.look(the_world)
        else:
            print(output('you cannot move there', 'yellow'))

    def move_north(self, the_world):
        self.move(lx=0, ly=-1, the_world=the_world, direction='north')

    def move_south(self, the_world):
        self.move(lx=0, ly=1, the_world=the_world, direction='south')

    def move_east(self, the_world):
        self.move(lx=1, ly=0, the_world=the_world, direction='east')

    def move_west(self, the_world):
        self.move(lx=-1, ly=0, the_world=the_world, direction='west')

    def take_item(self, the_world):
        pass

    def look(self, the_world):
        the_tile = the_world.tiles[(self.x, self.y)]
        print(output('{}'.format(the_tile[0]), 'green'))
        if len(the_tile) >= 2:
            print('')
            print(output('You see the following items:', 'green'))
            item_list = the_tile[1]
            for i in item_list:
                print(output('- {}'.format(i.name), 'green'))

    def examine_item(self, the_world):
        words_in_command = self.command.split()

        if len(words_in_command) == 1:
            print(output('Examine what?', 'yellow'))
        else:
            item_to_examine = words_in_command[1]
            the_tile = the_world.tiles[(self.x, self.y)]
            item_not_found = True

            if item_to_examine == 'self':
                print(output('{}'.format(self.name), 'green'))
                print(output('{}'.format(self.description), 'green'))

            elif len(the_tile) >= 2:
                item_list = the_tile[1]
                for i in item_list:
                    if i.name == item_to_examine:
                        print(output('{}'.format(i.description), 'green'))
                        item_not_found = False
                        break

                if item_not_found:
                    print(output("You don't see that.", 'yellow'))

            else:
                print(output("There is nothing to examine.", 'yellow'))

    def do_action(self, action, the_world):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(the_world)
