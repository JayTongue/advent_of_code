with open('2016/data/15.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().split('\n')]

discs = {}
for disc in data:
    number = int(disc[1][1:])
    positions = int(disc[3])
    start_pos = int(disc[-1][:-1])
    discs[number] = (positions, start_pos)
discs[7] = (11, 0)

def drop(offset, discs):
    for disc in range(1, max(discs.keys())+1):
        if (discs[disc][1]+disc+offset) % discs[disc][0] == 0:
            continue
        else:
            return False
    return True

offset = 0
while True:
    if drop(offset, discs):
        print(offset)
        break
    else:
        offset += 1
