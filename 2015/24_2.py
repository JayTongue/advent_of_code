import itertools
from math import prod

with open('2015/data/24.txt', 'r') as infile:
    data = sorted(list(map(int, infile.read().split('\n'))), reverse=True)

bucket_count = 4
bucket_size = sum(data)//bucket_count
bucket_combos = itertools.combinations(data, 4)
    
fits = set()
for bucket_combo in bucket_combos:
    if sum(bucket_combo) == bucket_size:
        fits.add(frozenset(bucket_combo))

qe = float('inf')
for f in fits:
    if len(f) == min(map(len, fits)):
        qe = min(qe, prod(f))
print(qe)