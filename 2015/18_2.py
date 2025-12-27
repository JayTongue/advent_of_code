from itertools import product

with open('2015/data/18.txt', 'r') as infile:
    data = [list(i) for i in infile.read().split('\n')]
row_max = len(data)-1 ; col_max = len(data[0])-1

def get_neighbors(row_idx, col_idx):
    row_fringes = [i for i in (row_idx+1, row_idx-1) if 0 <= i <= row_max]
    col_fringes = [j for j in (col_idx+1, col_idx-1) if 0 <= j <= col_max]
    neighbors = set(product(row_fringes+[row_idx], col_fringes+[col_idx]))
    neighbors.discard((row_idx, col_idx))
    return sum([data[r][c] == '#' for r, c in neighbors])

def fix_corners(grid):
    for x, y in ((0, 0), 
                 (len(grid)-1, 0), 
                 (0, len(grid)-1), 
                 (len(grid)-1, len(grid)-1)):
        grid[x][y] = '#'
    return grid

data = fix_corners(data)
for _ in range(100):
    new_grid = [['.'] * len(data[0]) for _ in range(len(data))]
    new_grid = fix_corners(new_grid)
    for row_idx in range(0, len(data)):
        for col_idx in range(0, len(data[0])):
            neighbor_count = get_neighbors(row_idx, col_idx)
            if all((data[row_idx][col_idx] == '#', neighbor_count in (2, 3))):
                new_grid[row_idx][col_idx] = '#'
            if data[row_idx][col_idx] == '.' and neighbor_count == 3:
                new_grid[row_idx][col_idx] = '#'
    data = new_grid
print(sum([i.count('#') for i in data]))
