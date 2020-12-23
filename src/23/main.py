
with open('input.txt') as f:
    data = [int(i) for i in f.read().strip()]


# "indexed" linked list with dict
class Node:
    def __init__(self, n, prev=None, next=None):
        self.n = n
        self.prev = prev
        self.next = next


def simulate(data, turns):
    nodes = {}

    # Build from input
    prev = None
    for i in data:
        node = Node(i, prev, None)
        if prev is not None:
            prev.next = node
        nodes[node.n] = node
        prev = node

    # Connect first and last
    last = prev
    first = nodes[data[0]]
    last.next = first
    first.prev = last

    curr = first
    for i in range(turns):
        c1 = curr.next
        c2 = c1.next
        c3 = c2.next

        # Remove c1, c2, c3 from list
        # Correct links
        curr.next = c3.next
        curr.next.prev = curr

        find = curr.n
        while True:
            find -= 1
            if find <= 0:
                find = len(data)
            if find not in (c1.n, c2.n, c3.n):
                break

        next = nodes[find]

        c3.next = next.next
        c3.next.prev = c3
        next.next = c1
        c1.prev = next

        curr = curr.next

    # Node with value 1
    return nodes[1]


# Part 1
res = ''
ptr = simulate(data, 100)
for i in data:
    ptr = ptr.next
    res += str(ptr.n)

print(res[:-1])

# Part 2
ptr = simulate(data + list(range(10, 1000000+1)), 10000000)
print(ptr.next.n * ptr.next.next.n)