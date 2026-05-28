with open('2017/data/19.txt', 'r') as infile:
    puz = infile.read().split('\n')
puz = [list(i) for i in puz]

start = (0, puz[0].index('|'))

def get_bubble(grid, coord):
    x, y = coord
    sides = [(i, j) for i, j in [(x, y-1), (x, y+1)] if 0<=i<=len(grid)-1 and 0<=j<=len(grid[0])-1 and grid[i][j] != ' ']
    tops = [(i, j) for i, j in [(x-1, y), (x+1, y)] if 0<=i<=len(grid)-1 and 0<=j<=len(grid[0])-1 and grid[i][j] != ' ']
    return {'-': sides, '|': tops}

seen = [start] ; mode, not_mode = '|', '-'
letters = []

while True:
    current = puz[start[0]][start[1]]
    if current == '+':
        mode, not_mode = not_mode, mode
    elif current.isupper():
        letters.append(current)
    paths = [i for i in get_bubble(puz, start)[mode] if i != seen[-1]]
    if len(paths) == 0:
        break
    elif len(paths) == 1:
        seen.append(start)
        start = paths[0]

print(len(seen))