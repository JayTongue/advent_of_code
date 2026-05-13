with open('2017/data/8.txt', 'r') as infile:
    steps = [i.split(' ') for i in infile.read().split('\n')]

registers = {} ; pointer = 0

while pointer < len(steps):
    step = steps[pointer]
    match = False
    step[2], step[-1] = int(step[2]), int(step[-1])
    for key in (step[0], step[4]):
        if key not in registers.keys():
            registers[key] = 0
    if step[5] == '>':
        if registers[step[4]] > step[6]:
            match = True
    elif step[5] == '<':
        if registers[step[4]] < step[6]:
            match = True
    elif step[5] == '>=':
        if registers[step[4]] >= step[6]:
            match = True
    elif step[5] == '<=':
        if registers[step[4]] <= step[6]:
            match = True
    elif step[5] == '!=':
        if registers[step[4]] != step[6]:
            match = True
    elif step[5] == '==':
        if registers[step[4]] == step[6]:
            match = True
    else:
        break
    if match:
        if step[1] == 'inc':
            registers[step[0]] += step[2]
        else:
            registers[step[0]] -= step[2]
    pointer += 1
print(sorted(registers.values())[-1])