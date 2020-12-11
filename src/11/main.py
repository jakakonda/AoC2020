IN = 'input.txt'
with open(IN, 'r') as f:
    data = [list(line) for line in f.read().splitlines()]

# Part 1
def get_state(data, y, x):
    Y = len(data)
    X = len(data[0])
    dd = [#dy, #dx
        (-1,  0), # above  
        (-1, +1), # above right
        ( 0, +1), # right
        (+1, +1), # bottom right
        (+1,  0), # bottom
        (+1, -1), # bottom left
        ( 0, -1), # left
        (-1, -1), # above left
    ]

    state = { '.': 0, '#': 0, 'L': 0}
    for d in dd:
        # Part 1
        # ny, nx = ny + d[0], nx + d[1]
        # if ny < 0 or nx < 0 or ny >= Y or nx >= X:
        #     continue
        # state[data[ny][nx]] += 1

        # Part 2
        ny, nx = y, x
        while True:
            ny, nx = ny + d[0], nx + d[1]
            if ny < 0 or nx < 0 or ny >= Y or nx >= X:
                break
            if data[ny][nx] == '.':
                continue
            state[data[ny][nx]] += 1
            break

    return state


def mutate_seat(data, y, x):
    state = get_state(data, y, x)

    if data[y][x] == 'L' and state['#'] == 0:
        return '#'
    if data[y][x] == '#'and state['#'] >= 5: # 4 for Part 1
        return 'L'

    return data[y][x]


def mutate(data):
    Y = len(data)
    X = len(data[0])
    changes = 1
    while changes > 0:
        new = []
        changes = 0
        for y in range(Y):
            new.append([])
            for x in range(X):
                new_seat = mutate_seat(data, y, x)
                new[y].append(new_seat)
                if data[y][x] != new_seat:
                    changes += 1

        data = new

    return data


no_seats = 0
final = mutate(data)
for row in final:
    for seat in row:
        if seat == '#':
            no_seats += 1

print(no_seats)

    
