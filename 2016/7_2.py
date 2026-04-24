import re
from itertools import combinations

with open('2016/data/7.txt', 'r') as infile:
    data = infile.read().split('\n')

sol = 0

def try_fit(ins, outs, mirrored, rev_mir):
    inner, outer = False, False
    if any(map(lambda x: mirrored in x, outs)):
        outer = True
    if any(map(lambda x: rev_mir in x, ins)):
        inner = True
    return inner, outer

for row in data:
    chars = set(list(row))
    row = re.split(r'\[|\]', row)
    ins = row[1::2] ; outs = row[0::2]
    outer, inner = False, False

    for combo in combinations(chars, 2):
        mirrored = ''.join(list(combo) + [combo[0]])
        rev_mir = ''.join([combo[-1]] + list(combo))

        if all(try_fit(ins, outs, mirrored, rev_mir)):
            sol += 1
            break
        else:
            mirrored, rev_mir = rev_mir, mirrored
            if all(try_fit(ins, outs, mirrored, rev_mir)):
                sol += 1
                break


print(sol)