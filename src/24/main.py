IN = 'input.txt'
with open(IN, 'r') as f:
    data = [line.strip() for line in f]

dirs = {
    "e":  (2, 0), 
    "se": (1, 1), 
    "w":  (-2, 0), 
    "nw": (-1, -1), 
    "ne": (1, -1), 
    "sw": (-1, 1)
}

def gen_neigh(coor):
    x, y = coor
    for d in dirs.values():
        yield (x + d[0], y + d[1])
    
def walk(path):
    idx = 0
    while idx < len(path):
        if path[idx] == 'e' or path[idx] == 'w':
            res = path[idx]
        else:
            res = path[idx:idx+2]
        idx += len(res)
        yield dirs[res]
        

# Part 1
grid = {}
for line in data:
    x, y = 0, 0
    for diff in walk(line):
        dx, dy = diff
        x += dx
        y += dy
    grid[(x, y)] = (grid.get((x, y), 0) + 1) % 2


print(sum(v for v in grid.values()))

# Part 2
def create_grid(grid):
    new = {}
    for coor, v in grid.items():
        neighs = gen_neigh(coor)
        for neigh in neighs:
            if neigh in grid:
                new[neigh] = grid[neigh]
            else:
                new[neigh] = 0
        new[coor] = v
    return new

def count_neigh(grid, coor):
    total = 0
    for neigh in gen_neigh(coor):
        if neigh in grid and grid[neigh] == 1:
            total += 1
    return total

# Create new grid from part 1, with neighrbous set to 0
# for calculation
grid = create_grid(grid)
for day in range(100):
    new = {}
    for coor, v in grid.items():
        blacks = count_neigh(grid, coor)
        new[coor] = grid[coor]
        if v == 1 and (blacks == 0 or blacks > 2):
            new[coor] = 0
        elif blacks == 2:
            new[coor] = 1
    grid = create_grid(new)

print(sum(v for v in grid.values()))
