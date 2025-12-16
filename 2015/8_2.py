import re

with open('2015/data/8.txt', 'r') as infile:
    data = infile.read().split('\n')

total = 0
for line in data:
    n_esc = len(re.findall(r'["\\]', line))
    total += (len(line) + n_esc + 2) - len(line)
print(total)
