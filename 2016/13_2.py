from collections import deque

with open('2016/data/13.txt', 'r') as infile:
    data = int(infile.read())

def is_open(x, y, data):
    return list(bin(x*x + 3*x + 2*x*y + y + y*y + data)).count('1') % 2 == 0

def next_steps(x, y):
    return ((x-1, y), (x+1, y), (x, y-1), (x, y+1))

def is_valid(x, y, grid):
    if 0<=x<=len(grid)-1 and 0<=y<=len(grid[0])-1:
        return grid[x][y]
    else:
        return False

grid_dims = (100, 100)
grid = [['.' for _ in range(grid_dims[1])] for _ in range(grid_dims[0])]

for i in range(grid_dims[0]):
    for j in range(grid_dims[1]):
        grid[i][j] = is_open(j,i, data)

coords = (1,1) ; steps = 0
dq = deque([(coords, steps)])
seen = set((1,1))

while True:
    current_coords, steps = dq.popleft()
    if steps > 48:
        break
    else:
        for x, y in next_steps(*current_coords):
            if is_valid(x, y, grid) and (x, y) not in seen:
                dq.append(((x, y), steps+1))
                seen.add((x, y))
print(len(seen))
