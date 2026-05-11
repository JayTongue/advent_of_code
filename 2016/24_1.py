from collections import deque
from itertools import permutations

with open('2016/data/24.txt', 'r') as infile:
    puz = [list(i) for i in infile.read().split('\n')]

numbers = {}
for row in range(len(puz)):
    numbers |= {i:(row, puz[row].index(i)) for i in puz[row] if i not in ['#', '.']}

def get_neighbors(puz, in_row, in_col):
    ret = []
    for out_row, out_col in [(in_row-1, in_col), (in_row, in_col-1), (in_row+1, in_col), (in_row, in_col+1)]:
        if 0<=out_row<=len(puz)-1 and 0<=out_col<=len(puz[0])-1: 
            ret.append((puz[out_row][out_col], (out_row, out_col)))
    return ret

cache = {} # only do each pair once
def go_from_to(puz, start:tuple, end:tuple, cache=cache):
    if (start, end) in cache.keys():
        return cache[(start, end)]
    dq = deque([(start, 0)]) # if not found, use BFS to find shortest path
    visited = set()
    while True:
        coord, step = dq.popleft()
        if coord == end:
            cache[(start, end)] = step 
            return step
        else:
            for dot, neigh_coord in get_neighbors(puz, *coord):
                if (dot.isdigit() or dot == '.') and neigh_coord not in visited:
                    dq.append((neigh_coord, step+1))
                    visited.add(neigh_coord)
                elif dot == '#':
                    continue

sol = float('inf')
for permu in permutations([i for i in numbers.keys() if i != '0']):
    total_steps = 0
    permu = ['0'] + list(permu)
    for idx in range(len(permu)-1):
        start = permu[idx] ; end = permu[idx+1]
        total_steps += go_from_to(puz, numbers[start], numbers[end])
    if total_steps < sol:
        sol = total_steps
print(sol)