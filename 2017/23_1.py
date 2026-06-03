from collections import defaultdict

registers = {i: 0 for i in list('abcdefgh')}

with open('2017/data/23.txt', 'r') as infile:
    commands = [i.split(' ') for i in infile.read().split('\n')]

def get_val(y):
    if y.strip('-').isdigit():
        return int(y)
    else:
        return registers[y]
pointer = 0 ; mul_count = 0
while 0 <= pointer < len(commands) :
    command, x, y = commands[pointer]
    if command == 'set':
        registers[x] = get_val(y)
    elif command == 'sub':
        registers[x] -= get_val(y)
    elif command == 'mul':
        registers[x] *= get_val(y)
        mul_count += 1
    elif command == 'jnz' and get_val(x) != 0:
        pointer += get_val(y) ; continue # skips incrementing pointer
    pointer += 1

print(mul_count)