seed = list('abcdefgh')

with open('2016/data/21.txt', 'r') as infile:
    instructions = infile.read().split('\n')

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
        if instruct[1] == 'left':
            for _ in range(int(instruct[2])):
                seed = seed[1:] + [seed[0]]
        elif instruct[1] == 'right':
            for _ in range(int(instruct[2])):
                seed = [seed[-1]] + seed[:-1]
        elif instruct[1] == 'based':
            idx = seed.index(instruct[-1])
            if idx < 4:
                for _ in range(idx+1):
                    seed = [seed[-1]] + seed[:-1]
            else: 
                for _ in range(idx+2):
                    seed = [seed[-1]] + seed[:-1]
    elif instruct[0] == 'move':
        x, y = int(instruct[2]), int(instruct[-1])
        x_char = seed[x]
        seed.pop(x) # remove thing from idx x
        seed.insert(y, x_char)
print(''.join(seed))