import re
from itertools import permutations

with open('2016/data/7.txt', 'r') as infile:
    data = infile.read().split('\n')

sol = 0
for row in data:
    chars = set(list(row))
    row = re.split(r'\[|\]', row)
    ins = row[1::2] ; outs = row[0::2]

    outer, inner = False, False
    for combo in permutations(chars, 2):
        mirrored = ''.join(combo + combo[::-1])
        if any(map(lambda x: mirrored in x, outs)):
            outer = True
        if any(map(lambda x: mirrored in x, ins)):
            inner = True
    if outer and not inner:
        sol += 1

print(sol)