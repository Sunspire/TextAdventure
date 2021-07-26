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
                    self.tiles[(xx, yy)] = cols[xx].replace('\n', '')

    def tile_exists(self, coords=(-1, -1)):
        if self.tiles.get(coords) is None:
            return False
        else:
            return self.tiles.get(coords) is not None