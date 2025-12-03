with open('2025/data/3.txt', 'r') as infile:
    data = infile.read().split('\n')

total = 0
for bank in data:
    bank = [int(i) for i in list(bank)]
    print(bank)
    one_val, one_idx = max(bank), bank.index(max(bank))
    
    if one_idx != len(bank)-1:
        bank = bank[one_idx+1:]
        two_val, two_idx = max(bank), bank.index(max(bank))
        largest = one_val * 10 + two_val
    else:
        bank = bank[:-1]
        two_val, two_idx = max(bank), bank.index(max(bank))
        largest = two_val * 10 + one_val
    total += largest
print(total)