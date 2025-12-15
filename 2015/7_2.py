from collections import defaultdict
import numpy as np
from copy import deepcopy

with open('2015/data/7.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().split('\n')]

data1 = deepcopy(data) ; data2 = deepcopy(data)
wires1 = defaultdict(lambda: np.uint16(0)) ; wires2 = defaultdict(lambda: np.uint16(0))
MASK = np.uint16(0xFFFF)

def solve_data(data, wires):
    if len(data) == 0:
        return data, wires

    remaining = []
    for d in data:
        changed = False

        if len(d) == 3:
            try:
                wires[d[2]] = np.uint16(int(d[0]))
                changed = True
            except ValueError:
                if d[0] in wires:
                    wires[d[2]] = np.uint16(wires[d[0]])
                    changed = True

        elif len(d) == 4:
            if d[1] in wires:
                wires[d[3]] = np.bitwise_not(np.uint16(wires[d[1]]))
                changed = True

        elif len(d) == 5:
            op = d[1]
            a, b, out = d[0], d[2], d[4]

            def val(tok):
                if tok.isdigit():
                    return np.uint16(int(tok))
                if tok in wires:
                    return np.uint16(wires[tok])
                return None

            if op == 'AND':
                va, vb = val(a), val(b)
                if va is not None and vb is not None:
                    wires[out] = np.uint16(va & vb)
                    changed = True

            elif op == 'OR':
                va, vb = val(a), val(b)
                if va is not None and vb is not None:
                    wires[out] = np.uint16(va | vb)
                    changed = True

            elif op == 'LSHIFT':
                va = val(a)
                if va is not None:
                    wires[out] = np.uint16((np.uint32(va) << int(b)) & 0xFFFF)
                    changed = True

            elif op == 'RSHIFT':
                va = val(a)
                if va is not None:
                    wires[out] = np.uint16(va >> int(b))
                    changed = True

        if not changed:
            remaining.append(d)

    return solve_data(remaining, wires)


remaining, wires1 = solve_data(data1, wires1)

for c, d in enumerate(data2):
    if d[1] == '->' and d[2] == 'b':
        data2[c] = [int(wires1['a']), '->', 'b']

remaining, wires2 = solve_data(data2, wires2)
print(wires2['a'])

