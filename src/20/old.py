# Over Engineered
# Would probably be faster

import numpy as np

tiles = {}
IN = 'input.txt'
with open(IN, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        tile_no = int(line.replace(':', '').strip().split()[1])
        tile = []
        read = False
        for line in f:
            line = line.strip()
            if not line:
                break
            tile.append(list(map(lambda c: c == '#', line)))

        tiles[tile_no] = np.array(tile)


class Transformation:
    def __init__(self, rotate=0, flipv=False, fliph=False):
        self.rotate = rotate
        self.flipv = flipv
        self.fliph = fliph

    def transform(self, tile):
        if self.fliph:
            tile = np.flip(tile, 0)
        if self.flipv:
            tile = np.flip(tile, 1)

        return np.rot90(tile, self.rotate)

    def __hash__(self):
        return (self.flipv, self.fliph, self.rotate)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"(v: {self.flipv}, h: {self.fliph}, r: {self.rotate})"


def gen_transforms():
    for v in [False, True]:
        for h in [False, True]:
            for r in range(4):
                # Prune
                if h == True and h == False and r == 2 or \
                   v == True and h == False and r == 3:
                    continue
                yield Transformation(r, v, h)

TOP = 't'
RIGHT = 'r'
LEFT  = 'l'
BOTTOM = 'b'

class Solver:
    def __init__(self, tiles: dict):
        self.tiles = tiles
        self.used = set()

    def _calc_possible(self):
        self.poss = {}

        def match_t(f, tile):
            for t in gen_transforms():
                tt = t.transform(tile)
                if (all(f(tt))):
                    yield t

        def add_dir(dir, id, f, tile):
            poss[dir][jk] = list(match_t(f, tile))
            if not poss[dir][jk]: 
                del poss[dir][jk]

        for ik, iv in self.tiles.items():
            poss = {
                TOP: {}, RIGHT: {}, BOTTOM: {}, LEFT: {}
            }
            for jk, jv in self.tiles.items():
                if ik == jk:
                    continue

                add_dir(TOP, jk, lambda t: iv[0,:] == t[0,:], jv)
                add_dir(RIGHT, jk, lambda t: iv[:,-1] == t[:,-1], jv)
                add_dir(BOTTOM, jk, lambda t: iv[-1,:] == t[-1,:], jv)
                add_dir(LEFT, jk, lambda t: iv[:,0] == t[:,0], jv)
            
            self.poss[ik] = poss

        # print(self.poss)

    def calc(self):
        used = set()
        self._calc_possible()
        n = int(math.sqrt(len(self.tiles)))
        grid = [[None] * n for _ in range(n)]

        def calc(y, x):
            for id, tile in self.tiles.items():
                if id in used:
                    continue

                used.add(id)

                used.remove(id)

solver = Solver(tiles)
solver.calc()           
