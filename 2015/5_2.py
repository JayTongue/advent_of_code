with open('2015/data/5.txt', 'r') as infile:
    data = infile.read().split('\n')

def find_two_pairs(d):
    return any([d.count(''.join((d[i], d[i+1]))) >=2 for i in range(len(d)-1)])

def find_sandwitches(d):
    return any([d[i] == d[i+2] for i in range(len(d)-2)])

nice = 0
for d in data:
    if all([find_two_pairs(d), find_sandwitches(d)]):
        nice += 1
print(nice)
