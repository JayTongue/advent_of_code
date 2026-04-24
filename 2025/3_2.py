from copy import deepcopy

with open('2025/data/3.txt', 'r') as infile:
    data = infile.read().split('\n')

total = 0
for bank in data:
    bank = [int(i) for i in list(bank)]
    largest = 0
    vals = []
    idx, cut_idx = -1, 0
    for i in range(11, -1, -1):
        idx += cut_idx + 1 
        if i == 0:
            i = -len(bank)
        cut_bank = deepcopy(bank)[idx:-i]
        cut_val, cut_idx = max(cut_bank), cut_bank.index(max(cut_bank))
        vals.append(cut_val)
    lexi = int(''.join(list(map(str, vals))))
    if largest < lexi:
        largest = lexi
    total += largest
print(total)