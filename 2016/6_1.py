from collections import Counter

with open('2016/data/6.txt', 'r') as infile:
    data = [list(i) for i in infile.read().split('\n')]

sol = []
for idx in range(len(data[0])):
    counter = Counter([j[idx] for j in data])
    sol.append(max(counter, key=counter.get))
print(''.join(sol))