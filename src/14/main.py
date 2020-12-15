import re
from functools import reduce


IN = 'input.txt'
with open(IN, 'r') as f:
    data = f.readlines()


def to_bin(mask, num):
    return '{0:b}'.format(int(num)).zfill(len(mask))

def mask_num(mask, num):
    num = list(to_bin(mask, num))

    for i in range(len(mask)):
       num[i] = num[i] if mask[i] == 'X' else mask[i]

    return ''.join(num)

# Part 1
mem = {}
mask = ''
for line in data:
    if line.startswith('mask'):
        mask = line.split('=')[1].strip()
    else:
        cmd = re.match("mem\[([0-9]+)] = ([\d]*)", line)
        mem[cmd[1]] = mask_num(mask, cmd[2])


total = reduce(lambda acc, x: acc + int(x, 2), mem.values(), 0)
print(total)

# Part 2
def mask_num(mask, num):
    num = list(to_bin(mask, num))
    for i in range(len(mask)):
       num[i] = num[i] if mask[i] == '0' else mask[i]

    return ''.join(num)

def gen_addr(mask, s=0):
    if s == len(mask):
        yield int(''.join(mask), 2)
        return
  
    if mask[s] == 'X':
        mask[s] = '0'
        yield from gen_addr(mask, s + 1)
        mask[s] = '1'
        yield from gen_addr(mask, s + 1)
        mask[s] = 'X'
    else:
        yield from gen_addr(mask, s + 1)


mem = {}
addrs = []
for line in data:
    if line.startswith('mask'):
        mask = line.split('=')[1].strip()
    else:
        cmd = re.match("mem\[([0-9]+)] = ([\d]*)", line)
        dst_mask = mask_num(mask, cmd[1])
        for addr in gen_addr(list(dst_mask)):
            mem[addr] = int(cmd[2])

total = reduce(lambda acc, x: acc + x, mem.values(), 0)
print(total)