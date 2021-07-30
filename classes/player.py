import functions.globals
import random
import time
from termcolor import colored
from classes.npc import Npc


class Player:
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp
        self.x = 0
        self.y = 0
        self.inventory = {}
        self.command = ''
        self.is_alive = True

    def __str__(self):
        return "{}, {}".format(self.name, self.hp)

    def item_exists(self, item):
        if self.inventory.get(item.name) is None:
            return False
        else:
            return True

    def move(self, lx, ly, direction):
        if not functions.globals.the_world.tile_exists((self.x + lx, self.y + ly)):
            print(colored('You cannot move there.', 'yellow'))
            return

        self.x += lx
        self.y += ly

        print(colored(f'You move {direction}.', 'green'))
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
            print(colored('Take what?', 'yellow'))
        else:
            item_to_take = words_in_command[1]
            the_tile = functions.globals.the_world.tiles[(self.x, self.y)]
            item_not_found = True
            item_list = the_tile.items
            if (item_list is not None and len(item_list) > 0):
                item_taken = None
                for item in item_list:
                    if item.name == item_to_take:
                        if self.item_exists(item):
                            print(colored('You already have that item.', 'yellow'))
                            item_not_found = False
                        else:
                            print(colored(f'You take: {item.name}.', 'green'))
                            self.inventory[item.name] = item
                            item_taken = item
                            item_not_found = False
                        break

                if item_taken is not None:
                    item_list.remove(item_taken)
                    the_tile.items = item_list
                    functions.globals.the_world.tiles[(self.x, self.y)] = the_tile

                if item_not_found:
                    print(colored("You don't find that.", 'yellow'))
            
            else:
                print(colored('There is nothing to take.', 'yellow'))

    def look(self):
        the_tile = functions.globals.the_world.tiles[(self.x, self.y)]
        print(colored(the_tile.description, 'green'))

        npc_list = the_tile.npcs
        if (npc_list is not None and len(npc_list) > 0):
            for npc in npc_list:
                print(colored(f'- {npc.description}', 'green'))

        item_list = the_tile.items
        if (item_list is not None and len(item_list) > 0):
            print()
            print(colored('You see the following items:', 'green'))
            for item in item_list:
                print(colored(f'- {item.name}', 'green'))

    def look_inventory(self):
        if len(self.inventory) == 0:
            print(colored('Your inventory is empty.', 'yellow'))
            return
        
        for item in self.inventory:
            print(colored(self.inventory[item].name + ' : ' + self.inventory[item].description, 'green'))
    
    def drop_inventory_item(self):
        if len(self.inventory) == 0:
            print(colored('Your inventory is empty.', 'yellow'))
            return

        words_in_command = self.command.split()

        if len(words_in_command) == 1:
            print(colored('Drop what?', 'yellow'))
        else:
            item_to_drop = words_in_command[1]
            item_not_found = True
            item_dropped = None
            inventory = self.inventory

            for item in inventory:
                if item_to_drop == inventory[item].name:
                    print(colored(f'you drop: {inventory[item].name}', 'green'))
                    item_dropped = inventory[item]
                    self.inventory.pop(item_to_drop)
                    item_not_found = False
                    break

            if item_dropped is not None:
                functions.globals.the_world.tiles[(self.x, self.y)].items.append(item_dropped)

            if item_not_found:
                print(colored("You don't have that item.", 'yellow'))

    def examine_item(self):
        words_in_command = self.command.split()

        if len(words_in_command) == 1:
            print(colored('Examine what?', 'yellow'))
            return

        item_to_examine = words_in_command[1]
        the_tile = functions.globals.the_world.tiles[(self.x, self.y)]

        if item_to_examine == 'self':
            print(colored(self.name, 'green'))
            print(colored(self.description, 'green'))
            return

        item_list = the_tile.items
        item_not_found = True
        if (item_list is not None and len(item_list) > 0):
            for item in item_list:
                if item.name == item_to_examine:
                    print(colored(item.description, 'green'))
                    item_not_found = False
                    break
        
        if item_not_found:
            print(colored("You don't see that.", 'yellow'))
    
    def attack_npc(self):
        words_in_command = self.command.split()

        if len(words_in_command) == 1:
            print(colored('Attack whom?', 'yellow'))
            return

        npc_to_attack = words_in_command[1]
        the_tile = functions.globals.the_world.tiles[(self.x, self.y)]
        npc_list = the_tile.npcs
        npc_not_found = True
        
        if (npc_list is not None and len(npc_list) > 0):
            for npc in npc_list:
                if npc.name == npc_to_attack:
                    print(colored(f'You attack: {npc.name}', 'yellow'))
                    npc = self.npc_fight(npc)
                    if npc.is_alive == False:
                        npc_list.remove(npc)
                    else:
                        npc_list[npc_list.index(npc)] = npc
                    
                    the_tile.npcs = npc_list
                    functions.globals.the_world.tiles[(self.x, self.y)] = the_tile
                    npc_not_found = False
                    break
        
        if npc_not_found:
            print(colored("You don't see that.", 'yellow'))

    def npc_fight(self, npc: Npc):
        start_time = time.time()
        interval = 0.5
        i = 0
        
        while (npc.is_alive or self.is_alive):
            time.sleep(start_time + i*interval - time.time())
            i += 0.5
            attack_priority = random.randrange(0,100)
            print(f'attack_priority: {attack_priority}')
            
            if attack_priority <= 50:
                npc.hp -= random.randrange(1,11)
            else:
                self.hp -= random.randrange(1,11)

            print(f'npc: {npc.hp}')
            print(f'you: {self.hp}')
            if npc.hp <= 0:
                print(colored(f'You slaughtered the {npc.name}', 'magenta'))
                npc.is_alive = False
                break
            
            if self.hp <= 0:
                print(colored(f'You died', 'red'))
                self.is_alive = False
                return npc
            
        return npc

    def do_action(self, action):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method()
