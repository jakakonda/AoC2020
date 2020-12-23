IN = 'input.txt'
decks = []
with open(IN, 'r') as f:
    for i in range(2):
        decks.append([])
        # Player N
        f.readline()
        for line in f:
            if not line.strip(): # Blank
                break
            decks[i].append(int(line.strip()))
        
# Part 1
def simulate(d0, d1):
    n = 0
    while len(d0) > 0 and len(d1) > 0:
        c0 = d0.pop(0)
        c1 = d1.pop(0)
        if c0 > c1:
            d0.append(c0)
            d0.append(c1)
        elif c1 > c0:
            d1.append(c1)
            d1.append(c0)
        else: #tie
            pass
        
        n += 1

    return (d0, d1)


d = simulate(decks[0].copy(), decks[1].copy())
idx = 0 if len(d[0]) > len(d[1]) else 1
total = 0
for i, n in enumerate(reversed(d[idx])):
    total += (i+1) * n

print(total)


# Part 2
def simulate_recursive(d0, d1, used):
    while(len(d0) > 0 and len(d1) > 0):
        game_id = (tuple(d0), tuple(d1))
        if game_id in used:
            return (0, d0)

        used.add(game_id)
        
        c0 = d0.pop(0)
        c1 = d1.pop(0)
        if len(d0) >= c0 and len(d1) >= c1:
            winner, _ = simulate_recursive(d0[:c0], d1[:c1], set())
        else:
            winner = 0 if c0 > c1 else 1

        if winner == 0:
            d0.append(c0)
            d0.append(c1)
        else:
            d1.append(c1)
            d1.append(c0)

    return (0, d0) if len(d0) > 0 else (1, d1)

_, d = simulate_recursive(decks[0].copy(), decks[1].copy(), set())
total = 0
for i, n in enumerate(reversed(d)):
    total += (i+1) * n

print(total)