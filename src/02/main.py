IN = 'input.txt'

with open(IN, 'r') as f:
    data = f.readlines()

def validate(line):
    parts = line.split(' ')
    bounds = list(map(int, parts[0].split('-')))
    ch = parts[1][0]
    pwd = parts[2].strip()
    
    # Part 1
    # count = pwd.count(ch)
    # return bounds[0] <= count and count <= bounds[1]

    # Part 2
    return (pwd[bounds[0]-1] == ch) ^ (pwd[bounds[1]-1] == ch)

valid = 0
for line in data:
    if (validate(line)):
        valid += 1

print(valid)