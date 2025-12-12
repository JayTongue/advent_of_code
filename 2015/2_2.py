from math import prod

with open('2015/data/2.txt', 'r') as infile:
    data = infile.read().split('\n')
    data = [list(map(int, i.split('x'))) for i in data]

print(sum([sum(sorted(box)[:2])*2 + prod(box) for box in data]))