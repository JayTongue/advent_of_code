seed = list('fbgdceah')

with open('2016/data/21.txt', 'r') as infile:
    instructions = reversed(infile.read().split('\n'))

for instruct in instructions:
    instruct = instruct.split(' ')
    if instruct[:2] == ['swap', 'position']:
        x, y = int(instruct[2]), int(instruct[-1])
        seed[x], seed[y] = seed[y], seed[x]
    elif instruct[:2] == ['swap', 'letter']:
        x, y = seed.index(instruct[2]), seed.index(instruct[-1])
        seed[x], seed[y] = seed[y], seed[x] 
    elif instruct[0] == 'reverse':
        x, y = int(instruct[2]), int(instruct[4])
        if x == 0:
            seed = seed[y::-1] + seed[y+1:]
        else:
            seed = seed[:x] + seed[y:x-1:-1] + seed[y+1:]
    elif instruct[0] == 'rotate':
        if instruct[1] == 'right':
            for _ in range(int(instruct[2])):
                seed = seed[1:] + [seed[0]]
        elif instruct[1] == 'left':
            for _ in range(int(instruct[2])):
                seed = [seed[-1]] + seed[:-1]
        elif instruct[1] == 'based':
            for i in range(len(seed)):
                candidate = seed[i:] + seed[:i]
                idx = candidate.index(instruct[-1])
                rot = (idx + 1 if idx < 4 else idx + 2) % len(seed)
                test = candidate[-rot:] + candidate[:-rot]
                if test == seed:
                    seed = candidate
                    break
    elif instruct[0] == 'move':
        x, y = int(instruct[2]), int(instruct[-1])
        y_char = seed[y]
        seed.pop(y)
        seed.insert(x, y_char)
print(''.join(seed))