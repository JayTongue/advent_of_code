with open('2017/data/4.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().split('\n')]

sol = 0
for d in data:
    d_frozen = set([frozenset(i) for i in d])
    if len(d_frozen) == len(d):
        sol += 1
print(sol)