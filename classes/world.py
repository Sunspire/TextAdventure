from classes.item import Item

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
                    self.tiles[(x, y)] = [cell.replace('\n', '')]

    def tile_exists(self, coords=(-1, -1)):
        return self.tiles.get(coords) is not None

    def test_override(self):
        self.tiles[(0, 0)] = [
            "You see a sign with the word \"TEST\" written on it.\n"
            "Various items are floating in the air.\n"
            "In the distance you see nothing but darkness.\n",
            [Item('cup', 'some foul smelling liquid is inside')
            ,Item('book', 'it contains drawings of legendary creatures')]
        ]
