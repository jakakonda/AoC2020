class Rule:
    def __init__(self, input):
        self.no = 0
        self.parse(input)
    
    def parse(self, input):
        n, rules = input.strip().split(':')
        self.no = int(n)

        if rules.strip()[0] == '"':
            self.isValue = True
            self.value = rules.replace('"', '').strip()
        else:
            self.isValue = False
            self.value = []
            for rule in rules.split('|'):
                self.value.append(list(map(int, rule.split())))

    def validate(self, rules, input, idx=0):
        if idx >= len(input):
            return (False, 0)

        if self.isValue:
            return (input[idx] == self.value, 1)

        valid = False
        skip = 0
        for g in self.value:
            res = None
            pos = idx
            for r in g:
                res = rules[r].validate(rules, input, pos)
                pos += res[1]
                if res[0] == False:
                    break

            if res[0] == True:
                valid = True
                skip = pos - idx
                break

        return (valid, skip)

rules = {}
inputs = []
IN = 'input.txt'
with open(IN, 'r') as f:
    for line in f:
        if line.strip() == '':
            break
        r = Rule(line)
        rules[r.no] = r
    
    for line in f:
        inputs.append(line.strip())


# Part 1
total = 0
for i in inputs:
    res = rules[0].validate(rules, i)
    if res[0] and res[1] == len(i):
        total += 1

print(total)


# Part 2
rules[8] = Rule('8: 42 | 42 8')
rules[11] = Rule('11: 42 31 | 42 11 31')

total = 0
for i in inputs:
    res = rules[0].validate(rules, i)
    if res[0] and res[1] == len(i):
        total += 1

print(total)