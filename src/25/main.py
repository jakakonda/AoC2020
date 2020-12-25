IN = 'input.txt'
with open(IN, 'r') as f:
    data = [int(line.strip()) for line in f]

n = 0
subject = 7
acc = 1
mod = 20201227

while acc != data[0]:
    acc = (acc*subject) % mod
    n += 1

print(pow(data[1], n, mod))
