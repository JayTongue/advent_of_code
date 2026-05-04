import re
from collections import deque

with open('2016/data/22.txt', 'r') as infile:
    data = [list(map(int, re.findall(r'\d+', i))) for i in infile.read().split('\n')[2:]]
    data = {(d[0], d[1]): d[2:] for d in data} # 0Size  1Used  2Avail  3Use

dim = max([i for i, j in data])
grid = [['v' for _ in range(dim+1)] for _ in range(dim+1)] # 0 to 30 inclusive

for d in data:
    if data[d][1] > 200: 
        grid[d[0]][d[1]] = 'w'
    elif data[d][1] == 0:
         grid[d[0]][d[1]] = 'h'
         hole = d

def get_neighbors(in_row, in_col):
    ret = []
    for row, col in [(in_row-1, in_col), 
              (in_row, in_col-1), 
              (in_row+1, in_col), 
              (in_row, in_col+1)]:
        if 0<=row<=dim and 0<=col<=dim:
            ret.append((row, col))
    return ret

dq = deque([(hole, 0)]) ; seen = {hole}
while True:
    coords, step = dq.popleft()
    if coords == (dim-1, 0):
        break
    else:
        neighbors = get_neighbors(*coords)
        for nrow, ncol in neighbors:
            if grid[nrow][ncol] != 'w' and (nrow, ncol) not in seen:
                dq.append(((nrow, ncol), step+1))
                seen.add((nrow, ncol))
print(step + (dim-1) * 5 +1)
