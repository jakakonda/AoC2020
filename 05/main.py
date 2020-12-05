import re

IN = 'input.txt'

with open(IN, 'r') as f:
    data = f.read().splitlines()

ids = []
for line in data:
    line = line.replace('B', '1').replace('F', '0')
    line = line.replace('R', '1').replace('L', '0')
    row = int(line[0:7], 2)
    col = int(line[-3:], 2)
    ids.append(row * 8 + col)

ids.sort()
for i in range(1, len(ids)):
    if ids[i - 1] + 1 != ids[i]:
        print(ids[i] - 1)
        break