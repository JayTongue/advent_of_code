import hashlib
from collections import deque

maze_dims = (4, 4)
start_coords = (0, 0) ; end_coords = (3, 3)

with open('2016/data/17.txt') as infile:
    starting_hash = infile.read()

def hashify(i):
    return hashlib.md5(i.encode()).hexdigest()

def cartesian(x, y):
    return {'U':(x-1, y), 
            'D':(x+1, y), 
            'L':(x, y-1), 
            'R':(x, y+1)}

def eval_open(i):
    return i in ['b', 'c', 'd', 'e', 'f']

def check_valid(row, col, has, k):
    if 0<=row<=maze_dims[0]-1 and 0<=col<=maze_dims[1]-1:
        if eval_open(hashify(has)[list('UDLR').index(k)]):
            return True
    return False

dq = deque([(start_coords, 0, starting_hash)])

longest = 0
while True:
    coords, step, has = dq.popleft()
    if coords == end_coords:
        if step > longest:
            longest = step
    else:
        for k, v in cartesian(*coords).items():
            if check_valid(*v, has, k):
                dq.append((v, step+1, f'{has}{k}'))
    if len(dq) == 0:
        break
print(longest)