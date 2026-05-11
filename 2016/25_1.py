from collections import defaultdict

with open('2016/data/25.txt', 'r') as infile:
    commands = [i.split(' ') for i in infile.read().split('\n')]

def is_int(s):
    try: int(s); return True
    except: return False

start_reg = 0 ; target = [0, 1] * 5 

while True:
    pointer_pos = 0 ; start_reg += 1
    registers = defaultdict(int) ; registers['a'] = start_reg
    emission = []
    while pointer_pos <= len(commands)-1:
        command = commands[pointer_pos]
        if command[0] == 'cpy':
            if is_int(command[1]):
                registers[command[2]] = int(command[1])
            else:
                registers[command[2]] = registers[command[1]]
        elif command[0] == 'dec':
            registers[command[1]] -= 1
        elif command[0] == 'inc':
            registers[command[1]] += 1
        elif command[0] == 'jnz':
            if (is_int(command[1]) and int(command[1]) != 0) or (not is_int(command[1]) and registers[command[1]] != 0) :
                if is_int(command[2]):
                    pointer_pos += int(command[2])
                else:
                    pointer_pos += registers[command[2]]
                continue # skips incrementing the pointer
            else:
                pass
        elif command[0] == 'out':
            emission.append(registers[command[1]])
            if emission != target[:len(emission)]:
                break
            if len(emission) == len(target):
                break
        pointer_pos += 1
        
    if emission == target:
        break
    else:
        continue
print(start_reg,)