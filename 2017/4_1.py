with open('2017/data/4.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().split('\n')]

print(sum(map(lambda x: len(set(x)) == len(x), data)))