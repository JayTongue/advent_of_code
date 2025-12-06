import re
from math import prod

with open('2025/data/6.txt', 'r') as infile:
    data = re.sub(r' +', ' ', infile.read())
    data = data.split('\n')
    data = [re.sub(r'^ | $', '', d).split(' ') for d in data]
    operators = data[-1]
    data = [list(map(int, i)) for i in data[:-1]]

sol = 0

for i in range(len(data[0])):
    if operators[i] == '+':
        sol += sum([d[i] for d in data])
    if operators[i] == '*':
        sol +=  prod([d[i] for d in data])
print(sol)