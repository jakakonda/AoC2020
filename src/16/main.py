rules = {}
my = []
nearby = []

IN = 'input.txt'
with open(IN, 'r') as f:
    # Rules
    for line in f:
        line = line.strip()
        if not line:
            break
        parts = line.split(':')
        p_rules = parts[1].split('or')
        p_rules = map(lambda r: r.strip().split('-'), p_rules)
        rules[parts[0]] = list(map(lambda r: (int(r[0]), int(r[1])), p_rules))

    # My
    f.readline()
    my = list(map(int, f.readline().strip().split(',')))

    # Nearby
    f.readline()
    f.readline()
    for line in f:
        line = line.strip()
        if not line:
            break
        nearby.append(list(map(int, line.strip().split(','))))


def validate(value, groups):
    for g, rules in groups.items():
        for rule in rules:
            if rule[0] <= value and value <= rule[1]:
                return True

    return False


# Part 1 with Part 2 filtering
total = 0
valid = []
for n in nearby:
    all_valid = True
    for f in n:
        if not validate(f, rules):
            total += f
            all_valid = False

    if all_valid:
        valid.append(n)


print(total)


# Part 2
def validate_field(value, rules):
    # only single rule group this time
    for rule in rules:
        if rule[0] <= value and value <= rule[1]:
            return True

    return False


def get_valid_fields_for_column(tickets, rules, i):
    cols = []
    for name, cond in rules.items():
        all_valid = True
        for t in tickets:
            if not validate_field(t[i], cond):
                all_valid = False
                break
        
        if all_valid:
            cols.append(name)

    return cols


possibilities = [get_valid_fields_for_column(valid, rules, i) for i in range(len(rules))]

def gen_rules(cols):
    def gen_internal(pref, cols, i):
        if i >= len(cols):
            yield pref
            return

        for col in cols[i]:
            if col not in pref:
                yield from gen_internal(pref + [col], cols, i+1)

    yield from gen_internal([], cols, 0)


valid_rules = None
for set in gen_rules(possibilities):
    print(set)
    valid_rules = set
    break

total = 1
for r, v in zip(valid_rules, my):
    if r.startswith('departure'):
        total *= v

print(total)