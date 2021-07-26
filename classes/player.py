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
        if not the_world.tile_exists((self.x + lx, self.y + ly)):
            print(output('you cannot move there', 'yellow'))
            return

        self.x += lx
        self.y += ly

        print(output(f'You move {direction}.', 'green'))
        self.look(the_world)

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
        print(output(the_tile[0], 'green'))

        if len(the_tile) < 2:
            return

        print()
        print(output('You see the following items:', 'green'))

        item_list = the_tile[1]
        for i in item_list:
            print(output(f'- {i.name}', 'green'))

    def examine_item(self, the_world):
        words_in_command = self.command.split()

        if len(words_in_command) == 1:
            print(output('Examine what?', 'yellow'))
            return

        item_to_examine = words_in_command[1]
        the_tile = the_world.tiles[(self.x, self.y)]

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

    def do_action(self, action, the_world):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(the_world)
