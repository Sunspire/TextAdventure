from classes.item import Item
from classes.item import Weapon
from classes.tile import Tile

the_world = None

class World:
    def __init__(self):
        self.tiles = {}

    def load_tiles(self):
        with open('resources/map.txt', 'r') as f:
            rows = f.readlines()

        for y, cols in enumerate(rows):
            for x, cell in enumerate(cols.split('\t')):
                if cell is not None:
                    the_tile = Tile()
                    the_tile.description = cell.replace('\n', '') 
                    self.tiles[(x, y)] = the_tile

    def tile_exists(self, coords=(-1, -1)):
        return self.tiles.get(coords) is not None

    def test_override(self):
        the_tile = Tile()
        the_tile.description = "You see a sign with the word \"TEST\" written on it.\n"\
                                "Various items are floating in the air.\n"\
                                "In the distance you see nothing but darkness.\n"
        the_tile.items = [
            Item('cup', 'some foul smelling liquid is inside')
            ,Item('book', 'it contains drawings of legendary creatures')
            ,Weapon('rusty_sword', 'a rusty sword with a dull blade')
        ]
        self.tiles[(0, 0)] = the_tile
