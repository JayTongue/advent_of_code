from itertools import permutations

with open('2017/data/2.txt', 'r') as infile:
    data = [list(map(int, d.split('\t'))) for d in infile.read().split('\n')]

sol = 0
for d in data:
    for c1, c2 in permutations(d, 2):
        if c1%c2 == 0:
            sol += c1//c2
            break

print(sol)