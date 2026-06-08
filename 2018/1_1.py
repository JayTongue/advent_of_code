with open('2018/data/1.txt', 'r') as infile:
    changes = infile.read().replace('+', '').split('\n')
changes = list(map(int, changes))

print(sum(changes))