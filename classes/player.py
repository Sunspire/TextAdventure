from functions.general import output
import functions.globals

class Player:
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp
        self.x = 0
        self.y = 0
        self.inventory = {}
        self.command = ''

    def __str__(self):
        return "{}, {}".format(self.name, self.hp)

    def item_exists(self, item):
        if self.inventory.get(item.name) is None:
            return False
        else:
            return True

    def move(self, lx, ly, direction):
        if not functions.globals.the_world.tile_exists((self.x + lx, self.y + ly)):
            print(output('you cannot move there', 'yellow'))
            return

        self.x += lx
        self.y += ly

        print(output('You move {}.'.format(direction), 'green'))
        self.look()

    def move_north(self):
        self.move(lx=0, ly=-1, direction='north')

    def move_south(self):
        self.move(lx=0, ly=1, direction='south')

    def move_east(self):
        self.move(lx=1, ly=0, direction='east')

    def move_west(self):
        self.move(lx=-1, ly=0, direction='west')

    def take_item(self):
        words_in_command = self.command.split()

        if len(words_in_command) == 1:
            print(output('Take what?', 'yellow'))
        else:
            item_to_take = words_in_command[1]
            the_tile = functions.globals.the_world.tiles[(self.x, self.y)]
            item_not_found = True
            if len(the_tile) >= 2:
                item_list = the_tile[1] 
                item_taken = None
                for item in item_list:
                    if item.name == item_to_take:
                        if self.item_exists(item):
                            print(output('You already have that item.', 'yellow'))
                            item_not_found = False
                        else:
                            print(output('You take: {}.'.format(item.name), 'green'))
                            self.inventory[item.name] = item
                            item_taken = item
                            item_not_found = False
                        break

                if item_taken is not None:
                    item_list.remove(item_taken)
                    the_tile[1] = item_list
                    functions.globals.the_world.tiles[(self.x, self.y)] = the_tile

                if item_not_found:
                    print(output("You don't find that.", 'yellow'))
            
            else:
                print(output('There is nothing to take.', 'yellow'))

    def look(self):
        the_tile = functions.globals.the_world.tiles[(self.x, self.y)]
        print(output(the_tile[0], 'green'))

        if len(the_tile) < 2:
            return

        print()
        print(output('You see the following items:', 'green'))

        item_list = the_tile[1]
        for i in item_list:
            print(output(f'- {i.name}', 'green'))

    def examine_item(self):
        words_in_command = self.command.split()

        if len(words_in_command) == 1:
            print(output('Examine what?', 'yellow'))
            return

        item_to_examine = words_in_command[1]
        the_tile = functions.globals.the_world.tiles[(self.x, self.y)]

        if item_to_examine == 'self':
            print(output(self.name, 'green'))
            print(output(self.description, 'green'))
            return

        if len(the_tile) < 2:
            print(output("There is nothing to examine.", 'yellow'))
            return

        item_list = the_tile[1]

        for i in item_list:
            if i.name == item_to_examine:
                print(output(i.description, 'green'))
                break
        else:
            print(output("You don't see that.", 'yellow'))

    def do_action(self, action):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method()
