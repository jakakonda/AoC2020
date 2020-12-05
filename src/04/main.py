import re

IN = 'input.txt'
with open(IN, 'r') as f:
    data = f.read().splitlines()

fields = {
    'byr': lambda v: no_between(v, 1920, 2002),
    'iyr': lambda v: no_between(v, 2010, 2020),
    'eyr': lambda v: no_between(v, 2020, 2030),
    'hgt': lambda v: validate_height(v),
    'hcl': lambda v: bool(re.match('^#([0-9a-f]{6})$', v)),
    'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda v: len(v) == 9 and v.isnumeric(),
    'cid': lambda v: True
}

def no_between(no, lower, upper):
    if not no.isnumeric():
        return False
    
    no = int(no)
    return lower <= no and no <= upper


def validate_height(str):
    unit = str[-2:]
    if unit == 'cm':
        return no_between(str[0:3], 150, 193)
    if unit == 'in':
        return no_between(str[0:2], 59, 76)
    return False


def validate(passport):
    has_fields = {}
    props = passport.split()
    for p in props:
        key, value = p.split(':')
        if key in fields and fields[key](value):
            has_fields[key] = True

    if len(has_fields) == len(fields):
        return True
    if len(has_fields) == len(fields) - 1 and 'cid' not in has_fields:
        return True

    return False
    

valid = 0
passport = ''
for line in data:
    # New passport
    if line == '':
        if validate(passport.strip()):
            valid += 1
        passport = ''
        
    passport += ' ' + line 

if validate(passport.strip()):
    valid += 1

print(valid)