with open('2015/data/23.txt', 'r') as infile:
    data = [i.split(' ') for i in infile.read().replace(',', '').replace('+', '').split('\n')]

reg = {'a': 0, 'b': 0}

def make_changes(reg, instr, idx):
    if instr[0] in ('hlf', 'tpl', 'inc'):
        if instr[0] == 'hlf':
            reg[instr[1]] //= 2
        elif instr[0] == 'tpl':
            reg[instr[1]] *= 3
        elif instr[0] == 'inc':
            reg[instr[1]] += 1
        idx += 1
    
    elif instr[0] in ('jie', 'jio'):
        if instr[0] == 'jie':
            if reg[instr[1]] % 2 == 0:
                idx += int(instr[2])
            else:
                idx += 1
        elif instr[0] == 'jio':
            if reg[instr[1]] == 1:
                idx += int(instr[2])
            else:
                idx += 1
        
    elif instr[0] == 'jmp':
        idx += int(instr[1])

    return reg, idx

idx = 0 
while 0 <= idx <= len(data)-1:
    reg, idx = make_changes(reg, data[idx], idx)
print(reg['b'])