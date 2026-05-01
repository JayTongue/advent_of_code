start, stop = 0, 4294967295

with open('2016/data/20.txt', 'r') as infile:
    block_ranges = sorted([(int(i.split('-')[0]), int(i.split('-')[1])) for i in infile.read().split('\n')])

existing_ranges = [block_ranges[0]]

for block_lo, block_hi in block_ranges[1:]:
    if block_lo <= existing_ranges[-1][1] + 1:
        existing_ranges[-1] = (existing_ranges[-1][0], max(block_hi, existing_ranges[-1][1]))
    else:
        existing_ranges.append((block_lo, block_hi))

print(existing_ranges[0][1]+1)
