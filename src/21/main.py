IN = 'input.txt'
data = []
with open(IN, 'r') as f:
    for line in f:
        ing, allg = line.strip().split('(contains')
        ing = [i.strip() for i in ing.split()]
        allg = [i.strip() for i in allg.replace(')', '').split(',')]
        data.append((ing, allg))

# Part 1
# Food count map
ings = {}
for food in data:
    for i in food[0]:
        ings[i] = ings.get(i, 0) + 1

# Each allergen is in excatly one
# Intersect known foods to find which one
# Each set has possible foods
algs_map = {}
for (ing, allg) in data:
    for a in allg:
        if a in algs_map:
            algs_map[a] = algs_map[a].intersection(ing)
        else:
            algs_map[a] = set(ing)

# The food must not be in any of the possible allergen foods
total = 0
for i in ings:
    if any([i in algs_map[k] for k in algs_map]):
        continue
    total += ings[i]

# print(total)

# Part 2
# find allergen with only one possibility
# Remove that alergen from all other possibilities
w2a_map = dict()

while len(w2a_map) != len(algs_map):
    for allg in algs_map:
        if allg in w2a_map:
            continue

        if len(algs_map[allg]) > 1:
            continue

        w, = algs_map[allg]
        w2a_map[allg] = w
        # Remove this from all others
        for a in algs_map:
            if a != allg:
                algs_map[a] = algs_map[a].difference(algs_map[allg])

ans = sorted(list(w2a_map.items()), key=lambda k: k[0]) 
print(','.join(list(map(lambda x: x[1], ans))))