with open('2025/data/7.txt', 'r') as infile:
    grid = [list(row) for row in infile.read().split('\n')]
    grid = [[0 if c == '.' else c for c in row] for row in grid]

rows = len(grid) ; cols = len(grid[0])
start_col = grid[0].index('S')
grid[1][start_col] = 1

for row in range(1, rows):
    old_row = grid[row]
    if row+1 < rows:
        new_row = [0 if isinstance(col, int) or col == '.' else col for col in grid[row+1]]
    
    for col in range(cols):
        if isinstance(old_row[col], int) and row+1 < rows:
            below = grid[row+1][col]
            if isinstance(below, int):
                new_row[col] += old_row[col]
        if old_row[col] == '^':
            incoming = grid[row-1][col]
            if isinstance(incoming, int):
                if col > 0 and isinstance(new_row[col-1], int):
                    new_row[col-1] += incoming
                if col < cols-1 and isinstance(new_row[col+1], int):
                    new_row[col+1] += incoming
    if row+1 < rows:
        grid[row+1] = new_row
print(sum([x for x in grid[-1] if isinstance(x, int)]))