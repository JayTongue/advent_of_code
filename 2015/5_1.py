with open('2015/data/5.txt', 'r') as infile:
    data = infile.read().split('\n')

def check_vowels(d):
    return sum(map(lambda x: d.count(x), list('aeiou'))) >= 3
def find_pairs(d):
    return not any(map(lambda x: x in d, ['ab', 'cd', 'pq', 'xy']))
def find_doubles(d):
    d = list(d)
    for i in range(len(d)-1):
        if d[i] == d[i+1]:
            return True
    return False

nice = 0
for d in data:
    if all([check_vowels(d), find_pairs(d), find_doubles(d)]):
        nice += 1
print(nice)
