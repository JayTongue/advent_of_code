import re

with open('2017/data/25.txt', 'r') as infile:
    instructs = infile.read().split('\n\n')

length = 9000
row = [0 for _ in range(length)] ; offset = length//2

state = re.findall(r'Begin in state (\w)\.', instructs[0])[0] ; steps = int(re.findall(r'after (.+?) steps\.', instructs[0])[0])

all_ins = {}
for ins in instructs[1:]:
    ins = ins.split('\n')
    if_state = re.findall(r'state (\w):', ins[0])[0]
    ins = ins[1:]
    blocks = {}
    for block in (ins[:len(ins)//2], ins[len(ins)//2:]):
        block = ''.join(block)
        key = int(re.findall(r'value is (\w):', block)[0])
        block = {'write': int(re.findall(r'the value (\w)\.', block)[0]), 
                 'move': re.findall(r'to the (.*?)\.', block)[0], 
                 'continue': re.findall(r'with state (\w)\.', block)[0]}
        if block['move'] == 'left':
            block['move'] = -1
        elif block['move'] == 'right':
            block['move'] = 1
        blocks[key] = block
    all_ins[if_state] = blocks

idx = 0 + offset
for i in range(steps):
    steps = all_ins[state][row[idx]]
    row[idx] = steps['write']
    idx += steps['move']
    state = steps['continue']

print(sum(row))

    