IN = 'input.txt'
with open(IN, 'r') as f:
    data = f.read().splitlines()  

index = {}

# Build index
# 'type color': { 'type color': no, ... }
for line in data:
    bag, contains = line.replace('.', '').split('contain')
    bag = ' '.join(bag.strip().split(' ')[:2])
    bags = contains.split(',')
    index[bag] = {}
    for b in bags:
        parts = b.strip().split(' ')
        if parts[0] != 'no':
            bag_in = ' '.join(parts[1:3])
            index[bag][bag_in] = int(parts[0])

# Part 1
def search(node):
    if 'shiny gold' in index[node]:
        return True

    for k, v in index[node].items():
        if search(k):
            return True

    return False


no_gold = 0
for key, _ in index.items():
    if (search(key)):
        no_gold += 1


print(no_gold)

# Part 2
def count_nested(node):
    total = 1
    for k, v in index[node].items():
        total += count_nested(k) * v

    return total

# Remove shiny gold since it was counted (- 1)
print(count_nested('shiny gold') - 1) 