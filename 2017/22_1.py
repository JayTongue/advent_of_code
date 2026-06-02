size = 50
grid = [['.' for _ in range(size)] for _ in range(size)]

with open('2017/data/22.txt', 'r') as outfile:
    puz = outfile.read().split('\n')
offset = size//2 - len(puz)//2

for row_idx, row in enumerate(puz):
    for i in range(len(row)):
        if row[i] == '#':
            grid[row_idx + offset][offset + i] = '#' 

def turn(current, direction):
    orientations = ['^', '>', 'v', '<']
    if direction == 'left':
        return orientations[orientations.index(current)-1]
    else:
        return orientations[(orientations.index(current)+1)%len(orientations)]

def move(current, direction):
    if direction == '^':
        return (current[0]-1, current[1])
    elif direction == '>':
        return (current[0], current[1]+1)
    elif direction == 'v':
        return (current[0]+1, current[1])
    elif direction == '<':
        return (current[0], current[1]-1)

virus_pos = (len(grid)//2, len(grid)//2) ; virus_ori = '^'
activated = 0
for _ in range(10_000):
    if grid[virus_pos[0]][virus_pos[1]] == '.':
        grid[virus_pos[0]][virus_pos[1]] = '#'
        new_direction = turn(virus_ori, 'left')
        moved = move(virus_pos, new_direction)
        activated += 1
    else:
        grid[virus_pos[0]][virus_pos[1]] = '.'
        new_direction = turn(virus_ori, 'right')
        moved = move(virus_pos, new_direction)

    virus_pos = moved ; virus_ori = new_direction

print(activated)