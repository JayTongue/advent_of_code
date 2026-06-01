def tuplify(x):
    if '/' in x:
        x = x.split('/')
    return tuple([tuple(i) for i in x])

with open('2017/data/21.txt', 'r') as infile:
    rules = infile.read().strip().split('\n')

rules = {tuplify(r.split(' => ')[0]): tuplify(r.split(' => ')[1]) for r in rules}

def rotate(grid): # rotates clockwise
    return [list(reversed([g[idx] for g in grid])) for idx in range(len(grid[0]))]

def reverse(grid): # reverses left to right
    return [list(reversed(g)) for g in grid]

def find_new(grid):
    for _ in range(2):
        for _ in range(4):
            if tuplify(grid) in rules:
                return rules[tuplify(grid)]
            grid = rotate(grid)

        grid = reverse(grid)

    raise Exception('No dict match')

puz = '''.#.
..#
###'''.split('\n')
puz = [list(p) for p in puz]

for _ in range(5):
    if len(puz) % 2 == 0:
        size = 2
    elif len(puz) % 3 == 0:
        size = 3

    blocks = []
    for row in range(0, len(puz), size):
        block_row = []
        for col in range(0, len(puz), size):
            grid = [r[col:col+size] for r in puz[row:row+size]]
            block_row.append(find_new(grid))
        blocks.append(block_row)

    new_puz = []
    for block_row in blocks:
        for inner_row in range(len(block_row[0])):
            new_puz.append([])

            for block in block_row:
                new_puz[-1] += list(block[inner_row])
    puz = new_puz

print(str(puz).count('#'))