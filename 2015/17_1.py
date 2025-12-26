from itertools import combinations

with open('2015/data/17.txt', 'r') as infile:
    buckets = list(map(int, infile.read().split('\n')))

sol = 0

for i in range(len(buckets)):
    for combo in combinations(buckets, i):
        if sum(combo) == 150:
            sol += 1
print(sol)