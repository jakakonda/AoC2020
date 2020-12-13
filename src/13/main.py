import math
from functools import reduce

IN = 'input.txt'
with open(IN, 'r') as f:
    t = int(f.readline().strip())
    data = f.readline().strip().split(',')
    data = {i:int(b) for i, b in enumerate(data) if b.isnumeric()}


# Part 1
bus = 0
min_wait = 10e12
for b in data.values():
    b = int(b)
    wait = b - t % b
    if wait < min_wait:
        bus = b
        min_wait = wait

print(min_wait * bus)


# Part 2
# Chinese remainder theorem gives us a 
# common reminder of all numbers
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i)*p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


n = data.values()
a = [bus - i for i, bus in data.items()]
print(chinese_remainder(n, a))
