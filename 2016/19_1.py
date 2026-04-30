with open('2016/data/19.txt', 'r') as infile:
    lim = int(infile.read())
skip = 2

def josephus(n, k, old):
    return (old+k) % n

enum_elves = [0]
for n_elves in range(2, lim+1):
    enum_elves.append(josephus(n_elves, skip, enum_elves[-1]))

print(enum_elves[-1]+1)
