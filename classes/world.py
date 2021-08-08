from classes.item import Armor, ArmorSlot, Item, ItemType, Weapon
from classes.tile import Tile
from classes.npc import Npc
from functions.general import is_json
import json


class World:
    def __init__(self):
        self.tiles = {}

    def load_tiles(self):
        with open('resources/map.txt', 'r') as f:
            rows = f.readlines()

            for y, cols in enumerate(rows):
                for x, cell in enumerate(cols.split('\t')):
                    if cell is not None:
                        json_string = cell
                        if is_json(json_string):
                            json_object = json.loads(json_string)
                            the_tile = Tile()
                            the_tile.reset_lists()
                            tile_items = json_object['tile_items']
                            tile_npcs = json_object['tile_npcs']
                            the_tile.description = str(json_object['tile_description'])

                            if len(tile_items) > 0:
                                for item in tile_items:
                                    the_item = None

                                    if item['item_type'] == ItemType.armor.name:
                                        pass

                                    elif item['item_type'] == ItemType.clutter.name:
                                        the_item = Item(item['item_name'], item['item_description'])
                                        the_item.value = int(item['item_value'])
                                        the_item.item_type = ItemType.clutter

                                    elif item['item_type'] == ItemType.weapon.name:
                                        the_item = Weapon(item['item_name'], item['item_description'])
                                        the_item.damage = int(item['item_damage'])
                                        the_item.item_type = ItemType.weapon
                                    
                                    if the_item is not None:
                                        the_tile.set_item(the_item)

                            if len(tile_npcs) > 0:
                                for npc in tile_npcs:
                                    the_npc = Npc()
                                    the_npc.name = npc['npc_name']
                                    the_npc.description = npc['npc_description']
                                    the_npc.pronoun = npc['npc_pronoun']
                                    the_npc.hp = int(npc['npc_hp'])
                                    the_npc.is_alive = True
                                    the_tile.set_npc(the_npc)

                            self.tiles[(x, y)] = the_tile

    def tile_exists(self, coords=(-1, -1)):
        return self.tiles.get(coords) is not None

    def test_override(self):

        the_npc = Npc('ruffian', 'a ruffian stares are you menacingly.')
        the_npc.hp = 75

        the_npc2 = Npc('thief', 'a thief crawls in the shadows.')
        the_npc3 = Npc('thief', 'another thief crawls in the shadows.')

        the_tile = Tile()
        the_tile.description = 'You see a sign with the word "TEST" written on it.\n'\
                                'Various items are floating in the air.\n'\
                                'In the distance you see nothing but darkness.\n'
        the_tile.items = [
            Item('cup', 'some foul smelling liquid is inside')
            ,Item('book', 'it contains drawings of legendary creatures')
            ,Weapon('rusty_sword', 'a rusty sword with a dull blade')
        ]

        the_tile.npcs = [the_npc,the_npc2,the_npc3]
        
        self.tiles[(0, 0)] = the_tile
