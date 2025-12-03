from itertools import combinations
# from tqdm import tqdm

with open('2025/data/3.txt', 'r') as infile:
    data = infile.read().split('\n')

total = 0
for bank in data:
    bank = [int(i) for i in list(bank)]
    
    largest = 0
    for combo in combinations(range(len(bank)), 12):
        trial_bank = [val for idx, val in enumerate(bank) if idx in combo]
        trial_sum = int(''.join(map(str, trial_bank)))
        if trial_sum > largest:
           largest = trial_sum

    total += largest
print(total)