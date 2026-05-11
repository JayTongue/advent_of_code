with open('2017/data/2.txt', 'r') as infile:
    data = [list(map(int, d.split('\t'))) for d in infile.read().split('\n')]

sol = 0
for d in data:
    sol += max(d) - min(d)

print(sol)
