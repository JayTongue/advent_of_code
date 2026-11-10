with open('2018/data/18.txt', 'r') as infile:
    grid = [list(i) for i in infile.read().split('\n')] 
print(len(grid), len(grid[0]))

def fetch_grid(point):
    return grid[point[0]][point[1]] 
def get_neighbors(point: tuple):
    def boundary(point):
        x, y = point
        return 0 <= x <= col-1 and 0 <= y <= row-1
    x, y = point
    row, col = len(grid), len(grid[0])
    possible_neighbors = [(x, y-1), 
                          (x, y+1), 
                          (x-1, y), 
                          (x+1, y),
                          (x-1, y-1),
                          (x-1, y+1), 
                          (x+1, y-1),
                          (x+1, y+1)]
    neighbors = filter(boundary, possible_neighbors)
    neighbors = map(fetch_grid, neighbors)
    return list(neighbors)

def next_pos(point, neighbors):
    if point == '.':
        if neighbors.count('|') >= 3:
            return '|'
        else:
            return point
    elif point == '|':
        if neighbors.count('#') >= 3:
            return '#'
        else:
            return point
    elif point == '#':
        if neighbors.count('#') >= 1 and neighbors.count('|') >= 1:
            return '#'
        else:
            return '.'

for _ in range(10): # embarassingly parallel problem
    grid_temp = [['' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            point = fetch_grid((row_idx, col_idx))
            neighbors = get_neighbors((row_idx, col_idx))
            next_dot = next_pos(point, neighbors)
            grid_temp[row_idx][col_idx] = next_dot
    grid = grid_temp
flattened = [j for i in grid for j in i]
print(flattened.count('#') * flattened.count('|'))
        
