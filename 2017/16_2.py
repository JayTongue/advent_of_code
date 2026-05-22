dancers = list('abcdefghijklmnop')
with open('2017/data/16.txt', 'r') as infile:
    commands = infile.read().split(',')

def dance(dancers):
    dancers = dancers[:]
    for command in commands:
        if command[0] == 's':
            chunk = int(command[1:])
            dancers = dancers[-chunk:] + dancers[:len(dancers)-chunk]
        elif command[0] == 'x':
            a_idx, b_idx = map(int, command[1:].split('/'))
            dancers[a_idx], dancers[b_idx] = dancers[b_idx], dancers[a_idx]
        elif command[0] == 'p':
            a_char, b_char = command[1:].split('/')
            a_idx, b_idx = dancers.index(a_char), dancers.index(b_char)
            dancers[a_idx], dancers[b_idx] = dancers[b_idx], dancers[a_idx]
    return dancers

start = list('abcdefghijklmnop')
cycle = [start[:]]
dancers = start[:]

while True:
    dancers = dance(dancers)
    if dancers == start:
        break
    cycle.append(dancers[:])

print(''.join(cycle[int(1e9) % len(cycle)]))

