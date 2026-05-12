from collections import Counter

with open('2017/data/6.txt', 'r') as infile:
    banks = [int(i) for i in infile.read().split('\t')]

seen_states = {tuple(banks):0}

while True:
    largest_val = max(banks)
    most_idx = banks.index(largest_val)
    for i in range(most_idx + 1, most_idx + largest_val+1):
        banks[i%len(banks)] += 1
    banks[most_idx] -= largest_val

    if tuple(banks) in seen_states.keys():
        break
    else:
        seen_states = {k: v+1 for k, v in seen_states.items()}
        seen_states[tuple(banks)] = 1

print(seen_states[tuple(banks)])