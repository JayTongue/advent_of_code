from collections import defaultdict

with open('2016/data/12.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().split('\n')]

registers = defaultdict(int)
registers['c'] = 1

pointer_pos = 0
while pointer_pos <= len(data)-1:
    command = data[pointer_pos]
    if command[0] == 'cpy':
        if command[1].isdigit():
            registers[command[2]] = int(command[1])
        else:
            registers[command[2]] = registers[command[1]]
    elif command[0] == 'inc':
        registers[command[1]] += 1
    elif command[0] == 'dec':
        registers[command[1]] -= 1
    elif command[0] == 'jnz':
        if (command[1].isdigit() and int(command[1]) != 0) or (not command[1].isdigit() and registers[command[1]] != 0) :
            pointer_pos += int(command[2])
            continue # skips incrementing the pointer
        else:
            pass
    pointer_pos += 1

print(registers['a'])