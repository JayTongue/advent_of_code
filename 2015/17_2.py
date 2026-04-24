from itertools import combinations

with open('2015/data/17.txt', 'r') as infile:
    buckets = list(map(int, infile.read().split('\n')))

min_containers = float('inf')

for i in range(len(buckets)):
    for combo in combinations(buckets, i):
        if sum(combo) == 150:
            min_containers = min(min_containers, len(combo))

sol = 0
for combo in combinations(buckets, min_containers):
    if sum(combo) == 150:
        sol += 1

print(sol)