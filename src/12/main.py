import math
import numpy as np

IN = 'input.txt'
with open(IN, 'r') as f:
    data = [(line[0], int(line[1:])) for line in f.read().splitlines()]


pos = ('E', 0, 0) # dir, north, east

# Part 1
def rotate(start, turns):
    dirs = ['N', 'E', 'S', 'W']
    return dirs[(dirs.index(start) + turns) % len(dirs)]

def move(cmd, p):
    if cmd[0] == 'N':
        return (p[0], p[1] + cmd[1], p[2])
    if cmd[0] == 'S':
        return (p[0], p[1] - cmd[1], p[2])
    if cmd[0] == 'E':
        return (p[0], p[1], p[2] + cmd[1])
    if cmd[0] == 'W':
        return (p[0], p[1], p[2] - cmd[1])
    if cmd[0] == 'L':
        return (rotate(p[0], -cmd[1] // 90), p[1], p[2])
    if cmd[0] == 'R':
        return (rotate(p[0], cmd[1] // 90), p[1], p[2])
    if cmd[0] == 'F':
        return move((p[0], cmd[1]), p)

for cmd in data:
    pos = move(cmd, pos)

print(abs(pos[1]) + abs(pos[2]))

# Part 2
# Pos is now a waypoint, not a ship,
# no need for direction
pos = ('E', 0, 0)
wpt = (1, 10)

# Use rotation matrix with translation
def rotate(pos, angle, pivot):
    angle = math.radians(angle)
    R = np.array([[math.cos(angle), - math.sin(angle), pivot[1]],
                  [math.sin(angle),   math.cos(angle), pivot[2]],
                  [               0,                 0,       1]])
    p = np.round(R.dot([[pos[0]], [pos[1]], [1]]))
    return (p[0][0] - pivot[1], p[1][0] - pivot[2])

def move(cmd, p, wpt):
    if cmd[0] == 'N':
        return p, (wpt[0] + cmd[1], wpt[1])
    if cmd[0] == 'S':
        return p, (wpt[0] - cmd[1], wpt[1])
    if cmd[0] == 'E':
        return p, (wpt[0], wpt[1] + 1)
    if cmd[0] == 'W':
        return p, (wpt[0], wpt[1] - 1)
    if cmd[0] == 'L':
        return p, rotate(wpt, -cmd[1], p)
    if cmd[0] == 'R':
        return p, rotate(wpt,  cmd[1], p)
    if cmd[0] == 'F':
        return (p[0], p[1] + wpt[0] * cmd[1], p[2] + wpt[1] * cmd[1]), wpt

for cmd in data:
    pos, wpt = move(cmd, pos, wpt)

print(abs(pos[1]) + abs(pos[2]))