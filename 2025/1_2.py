with open('2025/data/1.txt', 'r') as infile:
    raw = infile.read().split('\n')

def hits_in_move(pos, direction, steps, ring=100):
    step = 1 if direction == 'R' else -1

    if step == 1:
        n0 = (ring - pos) % ring
    else:
        n0 = pos % ring

    if n0 == 0:
        n0 = ring

    if n0 > steps:
        return 0
    return 1 + (steps - n0) // ring

def math_method(data):
    pos = 50
    count = 0
    for direction, steps in data:
        count += hits_in_move(pos, direction, steps, 100)
        step = 1 if direction == 'R' else -1
        pos = (pos + step * steps) % 100
    return count

data = [(t[0], int(t[1:])) for t in raw if t]

print(math_method(data))
