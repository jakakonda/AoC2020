IN = 'input.txt'
with open(IN, 'r') as f:
    data = list(map(int, f.readline().strip().split(',')))


last_spoken = { no: (i, i) for i, no in enumerate(data) } # turn

no = 0
for i in range(len(data), 30000000):
    t = last_spoken.get(no, (i, i))
    no = t[0] - t[1]

    if no not in last_spoken:
        last_spoken[no] = (i, i)
    else:
        last_spoken[no] = (i, last_spoken[no][0])
        
print(no)