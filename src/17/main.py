import itertools
import operator

# Initial grid size
grid = dict()
IN = 'input.txt'
with open(IN, 'r') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == '#':
                # Parth 1: grid[(0, y, x)] = 1
                grid[(0, 0, y, x)] = 1


def gen_neigh_coor(coor):
    # Part 1: repeat=3
    for d in itertools.product([-1, 0, 1], repeat=4):
        if all(map(lambda x: x == 0, d)):
            continue
        c = tuple(map(operator.add, coor, d))
        yield c


def count_neigh(grid, coor):
    total = 0
    for c in gen_neigh_coor(coor):
        if c in grid:
            total += 1
    return total


for i in range(6):
    next_coor = set()

    for coor in grid.keys():
        next_coor.add(coor)
        for c in gen_neigh_coor(coor):
            next_coor.add(c)

    neigh_count = {}
    for coor in next_coor:
        neigh_count[coor] = count_neigh(grid, coor)

    new = {}
    for coor in next_coor:
        v = grid.get(coor, 0)
        n = neigh_count[coor]
        if v == 1 and (n == 2 or n == 3):
            new[coor] = 1
        elif v == 0 and n == 3:
            new[coor] = 1

    grid = new


total = len(grid)
print(total)