from classes.item import Item


class World:
    def __init__(self):
        self.tiles = {}

    def load_tiles(self):
        with open('resources/map.txt', 'r') as f:
            rows = f.readlines()
            x_max = len(rows[0].split('\t'))

            for yy in range(len(rows)):
                cols = rows[yy].split('\t')
                for xx in range(x_max):
                    self.tiles[(xx, yy)] = [cols[xx].replace('\n', '')]

    def tile_exists(self, coords=(-1, -1)):
        return self.tiles.get(coords) is not None

    def test_override(self):
        cup = Item('cup', 'some foul smelling liquid is inside')
        book = Item('book', 'it contains drawings of legendary creatures')
        the_items = [cup, book]

        self.tiles[(0, 0)] = [
            "You see a sign with the word \"TEST\" written on it.\n"
            "Various items are floating in the air.\n"
            "In the distance you see nothing but darkness.\n",
            the_items
        ]
