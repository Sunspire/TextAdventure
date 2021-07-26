from classes.item import item

class world():
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
        if self.tiles.get(coords) is None:
            return False
        else:
            return self.tiles.get(coords) is not None

    def test_override(self):
        cup = item('cup', 'some foul smelling liquid is inside')
        book = item('book', 'it contains drawings of legendary creatures')
        the_items = [cup, book]
        self.tiles[(0,0)] = ['''You see a sign with the word "TEST" written on it.
Various items are floating in the air.
In the distance you see nothing but darkness.''', the_items]