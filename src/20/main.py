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

# Part 1
def gen_transform(tile):
    for r in range(4):
        arr = np.rot90(tile, k=r)
        yield arr
        yield np.flip(arr, 0)
        yield np.flip(arr, 1)
        yield np.flip(arr) # Both


n = int(np.sqrt(len(tiles)))

# Brute force
# All starting tiles
for tile_id in tiles:
    for tile in gen_transform(tiles[tile_id]):
        grid = [(tile_id, tile)]
        used = { tile_id }

        # Find next tile
        for y in range(1, len(tiles)):
            found_next = False
            for tile_num, tile in tiles.items():
                # Not yet used
                if tile_num in used: 
                    continue

                # Prev top and prev left constraints
                prev_top  = grid[y - n][1] if y // n != 0 else None
                prev_left = grid[y - 1][1] if y  % n != 0 else None

                for trans_tile in gen_transform(tile):
                    # Left
                    if prev_left is not None and not np.all(prev_left[:, -1] == trans_tile[:, 0]) or \
                       prev_top  is not None and not np.all( prev_top[-1, :] == trans_tile[0, :]):
                        continue

                    grid.append((tile_num, trans_tile))
                    used.add(tile_num)
                    found_next = True
                    break

            # The image is unique, only one combination, reset all
            if not found_next:
                break
        
        # Matched all
        if len(used) == len(tiles):
            break
    if len(used) == len(tiles):
        break

# Corners in flat array
print(grid[0][0] * grid[n - 1][0] * grid[n*n - n][0] * grid[n*n-1][0])

# Part 2
# Generate image 
size = grid[0][1].shape[0] - 2
img = np.zeros((size * n, size * n), dtype=bool)
for idx, cell in enumerate(grid):
    y = idx // n
    x = idx % n
    img[y*size:y*size+size, x*size:x*size+size] = cell[1][1:-1, 1:-1]


search = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]
search = np.array([list(map(lambda x: x == '#', line)) for line in search])

for img in gen_transform(img):
    total = 0
    mask = np.ones(img.shape) == True

    # Convolution
    for y in range(img.shape[0] - search.shape[0] + 1):
        for j in range(img.shape[1] - search.shape[1] + 1):
            img_slice = img[y:y + search.shape[0], j:j + search.shape[1]]
            if np.all((img_slice & search) == search):
                mask[y:y + search.shape[0], j:j + search.shape[1]] = search != True
                total += 1

    if total > 0:
        print(np.sum(img & mask))
        break