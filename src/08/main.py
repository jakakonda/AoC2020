IN = 'input.txt'
with open(IN, 'r') as f:
    data = f.read().splitlines()

# [(cmd, no), ...]
code = []
for line in data:
    split = line.strip().split(' ')
    code.append((split[0], int(split[1])))

def simulate(code):
    ptr = 0
    acc = 0
    exec_no = {} # { idx: no_visits }

    while ptr < len(code):
        cmd, val = code[ptr]
        if exec_no.get(ptr, 0) > 0:
            return (acc, False)

        exec_no[ptr] = exec_no.get(ptr, 0) + 1
        if cmd == 'nop':
            ptr += 1
        if cmd == 'acc':
            ptr += 1
            acc += val
        if cmd == 'jmp':
            ptr += val

    return (acc, True)

# Part 1
print(simulate(code))

# Part 2
for i in range(len(code)):
    # Modify
    org = code[i]
    if code[i][0] == 'nop':
        new = ('jmp', code[i][1])
    elif code[i][0] == 'jmp' and code[i][1] != 0:
        new = ('nop', code[i][1])
    else:
        continue

    code[i] = new
    
    # Simulate
    res = simulate(code)
    if res[1]:
        print(res)
        break

    # Restore
    code[i] = org