from collections import defaultdict, deque

with open('2017/data/18.txt', 'r') as infile:
    instructions = infile.read().strip().split('\n')

instructions = [i.split(' ') for i in instructions]

class prog:
    def __init__(self, pid):
        self.reg = defaultdict(int)
        self.reg['p'] = pid
        self.pointer = 0
        self.send_count = 0
        self.sendq = deque()
        self.deadlock = False
        self.other = False

prog_0 = prog(0) ; prog_1 = prog(1)
prog_0.other = prog_1 ; prog_1.other = prog_0

def two_numb(instruct, reg):
    if instruct[-1].lstrip('-').isdigit():
        return int(instruct[-1])
    return reg[instruct[-1]]

while True:
    progress = False

    for program in (prog_0, prog_1):
        program.deadlock = False

        if program.pointer < 0 or program.pointer >= len(instructions):
            program.deadlock = True
            continue

        instruct = instructions[program.pointer]
        if instruct[0] == 'set':
            program.reg[instruct[1]] = two_numb(instruct, program.reg)
        elif instruct[0] == 'add':
            program.reg[instruct[1]] += two_numb(instruct, program.reg)
        elif instruct[0] == 'mul':
            program.reg[instruct[1]] *= two_numb(instruct, program.reg)
        elif instruct[0] == 'mod':
            program.reg[instruct[1]] %= two_numb(instruct, program.reg)
        elif instruct[0] == 'snd':
            program.send_count += 1
            program.other.sendq.append(two_numb(instruct, program.reg))
        elif instruct[0] == 'rcv':
            if len(program.sendq) > 0:
                program.reg[instruct[1]] = program.sendq.popleft()
            else:
                program.deadlock = True
                continue
        elif instruct[0] == 'jgz':
            if two_numb([None, instruct[1]], program.reg) > 0:
                program.pointer += two_numb(instruct, program.reg)
                progress = True
                continue

        program.pointer += 1
        progress = True

    if not progress:
        break

print(prog_1.send_count)