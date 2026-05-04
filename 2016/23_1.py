from collections import defaultdict

with open('2016/data/23.txt', 'r') as infile:
    commands = [i.split(' ') for i in infile.read().split('\n')]

registers = defaultdict(int)
registers['a'] = 7

def is_int(s):
    try: int(s); return True
    except: return False

pointer_pos = 0
while pointer_pos <= len(commands)-1:
    command = commands[pointer_pos]
    if command[0] == 'cpy':
        if is_int(command[1]):
            registers[command[2]] = int(command[1])
        else:
            registers[command[2]] = registers[command[1]]
    elif command[0] == 'tgl':
        target_idx = registers[command[1]] + pointer_pos
        if 0 <= target_idx  <= len(commands) - 1:
            target = commands[target_idx]
            if len(target) == 2:
                if target[0] == 'inc':
                    commands[registers[command[1]]+ pointer_pos][0] = 'dec'
                else:
                    commands[registers[command[1]]+ pointer_pos][0] = 'inc'
            else:
                if target[0] == 'jnz':
                    commands[registers[command[1]]+ pointer_pos][0] = 'cpy'
                else:
                    commands[registers[command[1]]+ pointer_pos][0] = 'jnz'
    elif command[0] == 'inc':
        registers[command[1]] += 1
    elif command[0] == 'dec':
        registers[command[1]] -= 1
    elif command[0] == 'jnz':
        if (is_int(command[1]) and int(command[1]) != 0) or (not is_int(command[1]) and registers[command[1]] != 0) :
            if is_int(command[2]):
                pointer_pos += int(command[2])
            else:
                pointer_pos += registers[command[2]]
            continue # skips incrementing the pointer
        else:
            pass
    pointer_pos += 1
print(registers['a'])