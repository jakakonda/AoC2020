import itertools
import numpy as np

IN = 'input.txt'
LEN = 25
with open(IN, 'r') as f:
    data = list(map(int, f.read().splitlines()))


# Part 1
def has_sum(nums, target):
    for set in itertools.combinations(nums, 2):
        if (np.sum(set) == target):
            return True

    return False


no = 0
for i in range(LEN, len(data)):
    if not has_sum(data[i-LEN:i], data[i]):
        no = data[i]
        break

print (no)

# Part 2
for i in range(0, len(data)):
    total = 0
    for j in range(i, len(data)):
        total += data[j]
        if total == no:
            # Result
            print(min(data[i:j]) + max(data[i:j]))
            exit()
        if total > no:
            break