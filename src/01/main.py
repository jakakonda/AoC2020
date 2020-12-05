import itertools
import numpy as np

IN = 'input-n3.txt'

with open(IN, 'r') as f:
    data = list(map(int, f.readlines()))

for set in itertools.combinations(data, 3):
    if (np.sum(set) == 2020):
        print(np.prod(set))
        break