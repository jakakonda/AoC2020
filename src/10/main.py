import numpy as np

IN = 'input.txt'
LEN = 25
with open(IN, 'r') as f:
    data = list(map(int, f.read().splitlines()))

data.sort()
data.insert(0, 0) # from 0 to first adapter
data.append(data[-1] + 3) # from last to phone
diff = {} # { 3: 1 } # from last to phone

for i in range(1, len(data)):
    d = data[i] - data[i-1]
    diff[d] = diff.get(d, 0) + 1

print(diff.get(1, 0) * diff.get(3, 0))

# Part 2

# Count direct possibilities for each node
def count_possible(idx):
    total = 0
    for i in range(idx + 1, len(data)):
        d = data[i] - data[idx]
        if d > 3:
            break
        
        total += 1
    return total

# Sum direct valid (diff <= 3) descendants
poss = [count_possible(i) for i in range(len(data))]
def sum_possible(idx):
    total = 0
    for i in range(idx + 1, len(data)):
        d = data[i] - data[idx]
        if d > 3:
            break
        
        total += poss[i]

    return total

# Resolve sum of direct descendats beckwards
poss[-1] = 1
for i in reversed(range(len(data) - 1)):
    poss[i] = sum_possible(i)

print(poss[0])
