IN = 'input.txt'
with open(IN, 'r') as f:
    data = f.read().splitlines()

y = len(data)
x = len(data[0])

res = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] # (dx, dy)
for dx, dy in slopes:
    trees = 0
    for i, row in enumerate(range(0, y, dy)):
        if data[row][i * dx % x] == '#':
            trees += 1

    res *= trees

print(res)