dancers = list('abcdefghijklmnop')

with open('2017/data/16.txt', 'r') as infile:
    commands = infile.read().split(',')

for command in commands:
    if command[0] == 's':
        chunk = int(command[1:])
        dancers = dancers[-chunk:] + dancers[:len(dancers)-chunk]
    elif command[0] == 'x':
        a_idx, b_idx = tuple(map(int, command[1:].split('/')))
        dancers[a_idx], dancers[b_idx] = dancers[b_idx], dancers[a_idx]
    elif command[0] == 'p':
        a_char, b_char = tuple(command[1:].split('/'))
        a_idx, b_idx = dancers.index(a_char), dancers.index(b_char)
        dancers[a_idx], dancers[b_idx] = dancers[b_idx], dancers[a_idx]
print(''.join(dancers))