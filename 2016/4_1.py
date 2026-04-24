import re
from collections import Counter

with open('2016/data/4.txt', 'r') as infile:
    data = [re.split(r'\-|\[', re.sub(r']', '', i)) for i in infile.read().split('\n')]

sol = 0
for d in data:
    counts = Counter()
    for chunk in d[:-2]:
        for c in chunk:
            counts[c] += 1
    counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    checksum = []
    for i in range(counts[0][1], 0, -1):
        letters = [l[0] for l in counts if l[1] == i]
        checksum += sorted(letters)
    if d[-1] == ''.join(checksum[:5]):
       sol += int(d[-2])
print(sol) 