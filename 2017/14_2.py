from functools import reduce
from operator import xor

def knot_hash(in_str):
    string = list(range(256))
    lengths = [ord(l) for l in in_str] + [17, 31, 73, 47, 23]
    skip = 0 ; pointer = 0
    for _ in range(64):
        for length in lengths:
            window_idxs = [i % len(string) for i in range(pointer, pointer + length)]
            rev_window_vals = list(reversed([string[i] for i in window_idxs]))
            for flip, val in zip(window_idxs, rev_window_vals):
                string[flip] = val
            pointer = (pointer + length + skip) % len(string)
            skip += 1
    blocks = []
    for i in range(16):
        blocks.append(reduce(xor, [string[i * 16 + j] for j in range(16)]))
    return ''.join(format(b, '02x') for b in blocks)

def binify(start_string):
    return ''.join([str(bin(int(char, 16))[2:].zfill(4)) for char in list(start_string)])

start_str = 'ljoxqyyw'
starts = [f'{start_str}-{i}' for i in range(128)]
starts = [list(map(int, list(binify(b)))) for b in list(map(knot_hash, starts))]

def get_neighbors(x, y):
    valids = []
    if x>0:
        valids.append((x-1, y))
    if x<len(starts)-1:
        valids.append((x+1, y))
    if y>0:
        valids.append((x, y-1))
    if y<len(starts[0])-1:
        valids.append((x, y+1))
    valids = list(filter(lambda x: starts[x[0]][x[1]] == 1, valids))
    return valids

blob_count = 0
for row_idx in range(len(starts)):
    for col_idx in range(len(starts[0])):
        if starts[row_idx][col_idx] == 1:
            blob = set(get_neighbors(row_idx, col_idx))
            while True:
                changed = False
                for b in blob:
                    starts[b[0]][b[1]] = 2
                    neighbors = get_neighbors(*b)
                    if neighbors:
                        changed = True
                        new_blob = blob | set(neighbors)
                blob = new_blob
                if not changed:
                    break
            blob_count += 1
print(blob_count)
                
