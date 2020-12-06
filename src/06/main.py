IN = 'input.txt'
with open(IN, 'r') as f:
    data = f.read().splitlines()  

# Wrap the last input group
data.append('')

group = {}
no_people = 0
total = 0
for line in data:
    # New group
    if line == '':
        # Task 1
        # total += len(group) 
        # Task 2
        for _, v in group.items():
            if (v == no_people):
                total += 1
        group = {}
        no_people = 0
    else:
        no_people += 1
        for c in line:
            group[c] = group.get(c, 0) + 1

print(total)