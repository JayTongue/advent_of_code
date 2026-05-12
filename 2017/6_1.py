with open('2017/data/6.txt', 'r') as infile:
    banks = [int(i) for i in infile.read().split('\t')]

seen_states = set() ; steps = 1

while True:
    largest_val = max(banks)
    most_idx = banks.index(largest_val)
    for i in range(most_idx + 1, most_idx + largest_val+1):
        banks[i%len(banks)] += 1
    banks[most_idx] -= largest_val

    if tuple(banks) in seen_states:
        break
    else:
        steps += 1 ; seen_states.add(tuple(banks))

print(steps)