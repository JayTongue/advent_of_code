from collections import defaultdict
from itertools import permutations

with open('2015/data/13.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().split('\n')]

associations = defaultdict(dict)
for d in data:
    if d[2] == 'gain':
        associations[d[0]][d[-1][:-1]] = int(d[3])
    elif d[2] == 'lose':
        associations[d[0]][d[-1][:-1]] = -int(d[3])

happiness = 0
for perm in permutations(associations.keys()):
    arr_total = sum([associations[perm[idx]][perm[idx+1]] + 
                     associations[perm[idx+1]][perm[idx]] 
                     for idx in range(len(perm)-1)] + 
                     [associations[perm[-1]][perm[0]], 
                      associations[perm[0]][perm[-1]]])
    happiness = max(arr_total, happiness)
print(happiness)