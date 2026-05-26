from collections import defaultdict

with open('2017/data/18.txt', 'r') as infile:
    instructions = infile.read().split('\n')
instructions = [i.split(' ') for i in instructions]

registers = defaultdict(int)
sound = ''
pointer = 0

def two_numb(instruct):
    if instruct[-1].isdigit() or instruct[-1][0] == '-':
        return int(instruct[-1])
    return int(registers[instruct[-1]])

while True:
    if not 0 <= pointer < len(instructions):
        break

    instruct = instructions[pointer]
    if instruct[0] == 'set':
        registers[instruct[1]] = two_numb(instruct)
    elif instruct[0] == 'add':
        registers[instruct[1]] += two_numb(instruct)
    elif instruct[0] == 'mul':
        registers[instruct[1]] *= two_numb(instruct)
    elif instruct[0] == 'mod':
        registers[instruct[1]] = registers[instruct[1]] % two_numb(instruct)
    elif instruct[0] == 'snd':
        sound = registers[instruct[1]]
    elif instruct[0] == 'rcv':
        if two_numb(instruct[1]) > 0:
            break
    elif instruct[0] == 'jgz':
        if registers[instruct[1]] > 0:
            pointer += two_numb(instruct)-1
            
    pointer += 1
print(sound)